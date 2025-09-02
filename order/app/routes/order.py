from fastapi.routing import APIRouter
from app.schemas.order import OrderCreate,OrderOut,OrderUpdate
from app.models.order import OrderModel

router = APIRouter(prefix="/order",tags=["orders"])

@router.post("/create",response_model=OrderOut)
async def create_order(order:OrderCreate):
    order = order.model_dump()
    order_id = await OrderModel.create(order)
    return OrderOut(id=order_id,**order)



@router.put("/update")
async def update_order(order_detail:OrderUpdate):
    order_updated = await OrderModel.update(order_detail)
    return order_updated



