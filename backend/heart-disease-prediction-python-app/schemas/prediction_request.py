from pydantic import BaseModel, Field


class HeartPredictionRequest(BaseModel):

    age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Patient Age"
    )

    sex: int = Field(
        ...,
        ge=0,
        le=1,
        description="Gender (0=Female, 1=Male)"
    )

    dataset: int = Field(
        ...,
        ge=0,
        le=3,
        description="""
        Chest Pain Type:
        0 = Cleveland
        1 = Hungary
        2 = Switzerland
        3 = VA Long Beach
        """
    )

    cp: int = Field(
        ...,
        ge=0,
        le=3,
        description="""
        Chest Pain Type:
        0 = Typical Angina
        1 = Atypical Angina
        2 = Non-anginal Pain
        3 = Asymptomatic
        """
    )

    trestbps: float = Field(
        ...,
        ge=80,
        le=250,
        description="Resting Blood Pressure (mm Hg)"
    )

    chol: float = Field(
        ...,
        ge=100,
        le=700,
        description="Serum Cholesterol (mg/dl)"
    )

    fbs: int = Field(
        ...,
        ge=0,
        le=1,
        description="Fasting Blood Sugar >120 mg/dl"
    )

    restecg: int = Field(
        ...,
        ge=0,
        le=2,
        description="Resting ECG Results"
    )

    thalch: float = Field(
        ...,
        ge=50,
        le=250,
        description="Maximum Heart Rate Achieved"
    )

    exang: int = Field(
        ...,
        ge=0,
        le=1,
        description="Exercise Induced Angina"
    )

    oldpeak: float = Field(
        ...,
        ge=0,
        le=10,
        description="ST Depression"
    )

    slope: int = Field(
        ...,
        ge=0,
        le=2,
        description="Slope of Peak Exercise ST Segment"
    )

    ca: int = Field(
        ...,
        ge=0,
        le=4,
        description="Number of Major Vessels Colored"
    )

    thal: int = Field(
        ...,
        ge=0,
        le=3,
        description="""
        Thalassemia:
        0 = Normal
        1 = Fixed Defect
        2 = Reversible Defect
        3 = Unknown
        """
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "age": 63,
                "sex": 1,
                "cp": 3,
                "trestbps": 145,
                "chol": 233,
                "fbs": 1,
                "restecg": 0,
                "thalch": 150,
                "exang": 0,
                "oldpeak": 2.3,
                "slope": 0,
                "ca": 0,
                "thal": 1
            }
        }
    }