from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class Meal(BaseModel):
    idMeal: str = Field(alias="idMeal")
    strMeal: str = Field(alias="strMeal")
    strCategory: Optional[str] = Field(None, alias="strCategory")
    strArea: Optional[str] = Field(None, alias="strArea")
    strInstructions: Optional[str] = Field(None, alias="strInstructions")
    strMealThumb: Optional[HttpUrl] = Field(None, alias="strMealThumb")

    class Config:
        populate_by_name = True

class SearchResponse(BaseModel):
    meals: Optional[List[Meal]]