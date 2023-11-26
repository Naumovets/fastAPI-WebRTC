from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/pages', tags=['Pages'])

template = Jinja2Templates(directory='templates')


@router.get('/')
def get_index(request: Request):
    return template.TemplateResponse('index.html', {'request': request})


@router.get('/p2p/{room}')
def get_room(request: Request, room: str):
    return template.TemplateResponse('p2p.html', {'request': request, 'room': room})
