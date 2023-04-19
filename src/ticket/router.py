import asyncio
import time
from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
router = APIRouter()

@router.get("/parsian-naja-passport-status")
async def call_my_sync_library():
    my_data = await service.get_my_data()

    client = SyncAPIClient()
    await run_in_threadpool(client.make_request, data=my_data)
@router.get("/terrible-ping")
async def terrible_catastrophic_ping():
    time.sleep(10)  # I/O blocking operation for 10 seconds
    pong = service.get_pong()  # I/O blocking operation to get pong from DB

    return {"pong": pong}


@router.get("/good-ping")
def good_ping():
    time.sleep(10)  # I/O blocking operation for 10 seconds, but in another thread
    pong = service.get_pong()  # I/O blocking operation to get pong from DB, but in another thread

    return {"pong": pong}


@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10)  # non-blocking I/O operation
    pong = await service.async_get_pong()  # non-blocking I/O db call

    return {"pong": pong}
