import {
  Bar, BarChart, CartesianGrid, Cell, LabelList, Legend,
  Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis
} from "recharts";

type JsonObject = Record<string, unknown>;

const CHART_COLORS = ["#2563eb", "#ef4444", "#f59e0b", "#22c55e", "#8b5cf6", "#06b6d4", "#ec4899"];

const titleCase = (value: string) =>
  value.replaceAll("_", " ").replaceAll("-", " ").replace(/\b\w/g, c => c.toUpperCase());

const isPrimitive = (value: unknown) =>
  value === null || ["string", "number", "boolean"].includes(typeof value);

const formatValue = (value: unknown, key = "") => {
  if (value === null || value === undefined) return "N/A";
  if (typeof value === "number") {
    if (/rate|accuracy|percentage|percent/i.test(key))
      return `${value.toLocaleString(undefined, { maximumFractionDigits: 2 })}%`;
    return value.toLocaleString(undefined, { maximumFractionDigits: 3 });
  }
  if (typeof value === "boolean") return value ? "Yes" : "No";
  return String(value);
};

const MetricCards = ({ data }: { data: JsonObject }) => (
  <div className="metric-grid">
    {Object.entries(data).map(([key, value], index) => (
      <article className="metric-card" key={key}>
        <span className="metric-accent" style={{ background: CHART_COLORS[index % CHART_COLORS.length] }} />
        <span className="metric-label">{titleCase(key)}</span>
        <strong className="metric-value">{formatValue(value, key)}</strong>
      </article>
    ))}
  </div>
);

const ArrayTable = ({ data }: { data: JsonObject[] }) => {
  const columns = [...new Set(data.flatMap(item => Object.keys(item)))];
  return <div className="table-wrap"><table><thead><tr>
    {columns.map(c => <th key={c}>{titleCase(c)}</th>)}
  </tr></thead><tbody>{data.map((row, i) => <tr key={i}>
    {columns.map(c => <td key={c}>{isPrimitive(row[c]) ? formatValue(row[c], c) : JSON.stringify(row[c])}</td>)}
  </tr>)}</tbody></table></div>;
};

const TargetDistribution = ({ data }: { data: JsonObject }) => {
  const entries = Object.entries(data).filter(([,v]) => typeof v === "number");
  const disease = entries.find(([k]) => /heart.*disease|disease.*patient|positive/i.test(k));
  const healthy = entries.find(([k]) => /healthy|negative|no.*disease/i.test(k));
  if (!disease || !healthy) return null;
  const chartData = [
    { name: "Heart Disease", value: Number(disease[1]) },
    { name: "Healthy", value: Number(healthy[1]) }
  ];
  const total = chartData.reduce((s,x)=>s+x.value,0);
  return <div className="target-layout">
    <div className="donut-wrap">
      <ResponsiveContainer width="100%" height={340}>
        <PieChart>
          <Pie data={chartData} dataKey="value" nameKey="name" innerRadius={85} outerRadius={130} paddingAngle={2}>
            {chartData.map((_,i)=><Cell key={i} fill={i===0 ? "#ef476f" : "#22c55e"} />)}
          </Pie>
          <Tooltip formatter={(v:number)=>v.toLocaleString()} />
          <Legend verticalAlign="bottom" />
        </PieChart>
      </ResponsiveContainer>
      <div className="donut-center"><span>Total Patients</span><strong>{total.toLocaleString()}</strong></div>
    </div>
    <div className="distribution-summary">
      {chartData.map((item,i)=><div className="distribution-row" key={item.name}>
        <span className="distribution-dot" style={{background:i===0?"#ef476f":"#22c55e"}}/>
        <div><span>{item.name}</span><strong>{item.value.toLocaleString()}</strong>
          <small>{total ? ((item.value/total)*100).toFixed(1) : 0}% of patients</small>
        </div>
      </div>)}
    </div>
  </div>;
};

const KpiVisual = ({ data }: { data: JsonObject }) => {
  const numeric = Object.entries(data).filter(([,v]) => typeof v === "number");
  const counts = numeric.filter(([k,v]) => !/rate|accuracy|percentage|percent|auc/i.test(k) && Number(v) > 1)
    .map(([name,value])=>({name:titleCase(name),value:Number(value),key:name}));
  const performance = numeric.filter(([k]) => /rate|accuracy|percentage|percent|auc/i.test(k))
    .map(([name,value])=>({name:titleCase(name),value:Number(value),key:name}));

  return <div className="kpi-visuals">
    {counts.length > 0 && <div className="chart-panel">
      <div className="chart-heading"><div><h3>Patient Risk Overview</h3><p>Patient volume and risk-group distribution</p></div></div>
      <ResponsiveContainer width="100%" height={360}>
        <BarChart data={counts} margin={{top:25,right:20,left:5,bottom:55}}>
          <CartesianGrid strokeDasharray="3 3" vertical={false}/>
          <XAxis dataKey="name" angle={-20} textAnchor="end" interval={0} height={75}/>
          <YAxis/>
          <Tooltip formatter={(v:number)=>v.toLocaleString()}/>
          <Bar dataKey="value" radius={[8,8,0,0]}>
            {counts.map((_,i)=><Cell key={i} fill={CHART_COLORS[i % CHART_COLORS.length]}/>)}
            <LabelList dataKey="value" position="top" formatter={(v:number)=>v.toLocaleString()}/>
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>}
    {performance.length > 0 && <div className="performance-grid">
      {performance.map((item,i)=>{
        const normalized=/auc/i.test(item.key) && item.value <= 1 ? item.value*100 : item.value;
        return <article className="performance-card" key={item.key}>
          <span>{item.name}</span><strong>{formatValue(item.value,item.key)}</strong>
          <div className="progress-track"><div className="progress-fill" style={{width:`${Math.min(normalized,100)}%`,background:CHART_COLORS[(i+4)%CHART_COLORS.length]}}/></div>
          <small>{normalized >= 90 ? "Excellent" : normalized >= 80 ? "Strong" : normalized >= 70 ? "Good" : "Needs attention"}</small>
        </article>
      })}
    </div>}
  </div>;
};

const RiskBars = ({ data }: { data: JsonObject }) => {
  const rows=Object.entries(data).filter(([,v])=>typeof v==="number")
    .map(([label,value])=>({label,value:Number(value)})).sort((a,b)=>b.value-a.value);
  const max=Math.max(...rows.map(r=>r.value),1);
  return <div className="risk-list">{rows.map((row,index)=><div className="risk-row" key={row.label}>
    <div className="risk-heading"><strong>#{index+1} {titleCase(row.label)}</strong><span>{formatValue(row.value,row.label)}</span></div>
    <div className="risk-track"><div className={`risk-fill priority-${Math.min(index+1,4)}`} style={{width:`${row.value/max*100}%`}}/></div>
    <small>{index===0?"Highest priority":index===1?"High priority":"Priority risk factor"}</small>
  </div>)}</div>;
};

const Section = ({ name, value }: { name:string; value:unknown }) => {
  if (Array.isArray(value)) {
    if (!value.length) return <section className="content-card"><h2 className="section-title">{titleCase(name)}</h2><p>No data available.</p></section>;
    if (value.every(v=>typeof v==="object" && v!==null && !Array.isArray(v)))
      return <section className="content-card full-width"><h2 className="section-title">{titleCase(name)}</h2><ArrayTable data={value as JsonObject[]}/></section>;
    return <section className="content-card text-section"><h2 className="section-title">{titleCase(name)}</h2><div className="markdown-list">
      {value.map((v,i)=><div className="markdown-item" key={i}><span className="item-index">{i+1}</span><p>{formatValue(v)}</p></div>)}
    </div></section>;
  }
  if (typeof value==="object" && value!==null) {
    const object=value as JsonObject;
    const primitives=Object.values(object).every(isPrimitive);
    if (/target.*distribution/i.test(name)) return <section className="content-card full-width"><h2 className="section-title">{titleCase(name)}</h2><TargetDistribution data={object}/></section>;
    if (/kpi/i.test(name)) return <section className="content-card full-width"><h2 className="section-title">{titleCase(name)}</h2><MetricCards data={object}/><KpiVisual data={object}/></section>;
    return <section className="content-card"><h2 className="section-title">{titleCase(name)}</h2>
      {primitives ? (/risk|factor|severity|probability|score/i.test(name) ? <RiskBars data={object}/> : <MetricCards data={object}/>) :
      <div className="nested-grid">{Object.entries(object).map(([k,v])=><Section key={k} name={k} value={v}/>)}</div>}
    </section>;
  }
  return <article className="metric-card"><span className="metric-label">{titleCase(name)}</span><strong className="metric-value">{formatValue(value,name)}</strong></article>;
};

export const ResponseView = ({ data }: { data:unknown }) => {
  if (data===null || data===undefined) return null;
  if (Array.isArray(data)) {
    if (data.every(v=>typeof v==="object" && v!==null && !Array.isArray(v))) return <ArrayTable data={data as JsonObject[]}/>;
    return <div className="markdown-list">{data.map((v,i)=><div className="markdown-item" key={i}><span className="item-index">{i+1}</span><p>{formatValue(v)}</p></div>)}</div>;
  }
  if (typeof data==="object") {
    const object=data as JsonObject;
    const primitives=Object.values(object).every(isPrimitive);
    if (primitives) return <MetricCards data={object}/>;
    return <div className="response-grid">{Object.entries(object).map(([k,v])=><Section key={k} name={k} value={v}/>)}</div>;
  }
  return <div className="content-card">{formatValue(data)}</div>;
};
