from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.
# 요청이 들어오면 인덱스를 실행시켜 라는 의미
def index(request):
    #입력인자
    page = request.GET.get('page', 1)       #설정이 없으면 1로 페이지 설정
    #조회
    board_list = Board.objects.order_by('-create_date')
    #페이징 처리
    paginator = Paginator(board_list, 5)    #5개씩 쪼개서 출력한다는 의미
    page_obj = paginator.get_page(page)
    context = {'board_list' : page_obj}
    #context = {'board_list' : board_list}
    #return HttpResponse("bbsnote에 오신것을 환영합니다!!");
    return render(request, 'bbsnote/board_list.html',context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id) 
    context = {'board': board}
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id): 
    board = Board.objects.get(id=board_id)
    #comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    #comment.save()
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('bbsnote:detail', board_id=board.id)

def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST) 
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index') 
    else:
        form = BoardForm()
        return render(request, 'bbsnote/board_form.html', {'form':form})
        