from fastapi import FastAPI
app = FastAPI()

DATABASE =[
    {
        "id" : 1,
        "name" : "Rahul",
        "branch" : "Computer science"
    },
    {
        "id" : 2,
        "name" : "Karan",
        "branch" : "information technology"
    },
    {
        "id" : 3,
        "name" : "Gagan",
        "branch" : "Data science"
    },
    {
        "id" : 4,
        "name" : "sumit",
        "branch" : "AI/ML"
    }
]
# all data return 
@app.get("/product")
async def all_product():
    return DATABASE

# single data return 
@app.get("/product/{product_id}")
async def single_product(product_id : int):
    for product in DATABASE :
        if product["id"] == product_id:
            return product
    return {"message": "product not found"}



# post method (create data) 
@app.post("/Create")
async def add_data(new_product : dict):
    DATABASE.append(new_product)
    return{
        "status":new_product
    }
# put method Use to fully update data
@app.put("/product/{product_id}")
async def update_data(product_id : int , new_updated_data : dict):
    for index,product in enumerate(DATABASE):
        if product["id"] == product_id:
            DATABASE[index] = new_updated_data
            return {
                "status": "updated",
                "product_id": product_id,
                "new_updated_data": new_updated_data
            }
    return {"message": "product not found"}

# patch method partially update
@app.patch("/product/{product_id}")
async def update_data(product_id : int , new_updated_data : dict):
    for index,product in enumerate(DATABASE):
        if product["id"] == product_id:
            DATABASE[index] = new_updated_data
            return {
                "status": "updated",
                "product_id": product_id,
                "new_updated_data": new_updated_data
            }
    return {"message": "product not found"}
# delete method (delete data)
@app.delete("/product/{product_id}")
async def deleted(product_id : int):
    for index, product in enumerate(DATABASE):
        if product["id"] == product_id:
            DATABASE.pop(index)
    return{
        "response" : "delete data" , "product_id" : product_id
    }