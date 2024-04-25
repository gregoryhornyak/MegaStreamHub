class video_model:
    def __init__(self, _ID:str,_title:str,_size:str,_duration:int,_author:str,_date:str,_genre:list,_res:str,_caption:list,_descr:str) -> None:
        self.ID = _ID
        self.title = _title
        self.size = _size
        self.duration = _duration
        self.author = _author
        self.date = _date
        self.genre = _genre
        self.resolution = _res
        self.caption = _caption
        self.description = _descr
        
