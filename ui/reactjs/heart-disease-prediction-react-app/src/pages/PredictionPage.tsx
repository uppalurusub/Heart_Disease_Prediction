import { FormEvent, useEffect, useState } from "react";
import { heartApi } from "../api/heartApi";
import { http } from "../api/http";
import { ResponseView } from "../components/common/ResponseView";

type SchemaProperty = { title?: string; type?: string; default?: unknown; minimum?: number; maximum?: number; enum?: unknown[]; anyOf?: SchemaProperty[] };
type ApiSchema = { required?: string[]; properties?: Record<string, SchemaProperty> };

const label = (v:string) => v.replaceAll("_"," ").replace(/\b\w/g,c=>c.toUpperCase());

export const PredictionPage = () => {
  const [schema,setSchema]=useState<ApiSchema>({});
  const [form,setForm]=useState<Record<string,unknown>>({});
  const [result,setResult]=useState<unknown>();
  const [error,setError]=useState("");

  useEffect(()=>{
    http.get("/openapi.json").then(({data})=>{
      const ref=data.paths?.["/heart/predict"]?.post?.requestBody?.content?.["application/json"]?.schema?.["$ref"];
      const name=ref?.split("/").pop();
      const model:ApiSchema=data.components?.schemas?.[name] ?? {};
      setSchema(model);
      const initial:Record<string,unknown>={};
      Object.entries(model.properties ?? {}).forEach(([key,p])=>{
        initial[key]=p.default ?? (p.type==="string" ? "" : 0);
      });
      setForm(initial);
    }).catch(()=>setError("Unable to load prediction schema from FastAPI OpenAPI."));
  },[]);

  const submit=async(e:FormEvent)=>{
    e.preventDefault(); setError("");
    try { setResult(await heartApi.predict(form as never)); }
    catch(err:any) {
      const detail=err?.response?.data?.detail;
      setError(Array.isArray(detail) ? detail.map((d:any)=>`${d.loc?.slice(1).join(".")}: ${d.msg}`).join(" | ") : err?.message ?? "Prediction failed");
    }
  };

  return <div className="page">
    <div className="page-header"><span className="eyebrow">Clinical AI</span><h1>Heart Disease Risk Prediction</h1><p>Complete all required clinical attributes. Fields are loaded directly from the FastAPI <strong>HeartPredictionRequest</strong> schema to prevent request mismatch.</p></div>
    {error && <div className="error-banner"><strong>Prediction request error</strong><p>{error}</p></div>}
    <form className="prediction-form content-card" onSubmit={submit}>
      <h2 className="section-title">Patient Clinical Inputs</h2>
      <div className="input-grid">
      {Object.entries(schema.properties ?? {}).map(([key,p])=>{
        const required=schema.required?.includes(key);
        return <label className="field" key={key}><span>{label(key)} {required&&<b>*</b>}</span>
          {p.enum ? <select required={required} value={String(form[key] ?? "")} onChange={e=>setForm({...form,[key]:e.target.value})}>{p.enum.map(v=><option key={String(v)} value={String(v)}>{String(v)}</option>)}</select> :
          <input required={required} type={p.type==="string"?"text":"number"} step="any" min={p.minimum} max={p.maximum} value={String(form[key] ?? "")} onChange={e=>setForm({...form,[key]:p.type==="string"?e.target.value:Number(e.target.value)})}/>}
        </label>
      })}
      </div>
      <button className="predict-button" type="submit">Predict Heart Disease Risk</button>
    </form>
    {result !== undefined && <section className="result-section"><h2>Prediction Result</h2><ResponseView data={result}/></section>}
  </div>;
};
