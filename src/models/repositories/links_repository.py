from sqlite3 import Connection
from typing import Dict, Tuple, List

class LinksRepository():
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def add_links(self, links_infos: Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''',(
                links_infos["id"],
                links_infos["trip_id"],
                links_infos["link"],
                links_infos["title"],
                
            )
        )
        self.__conn.commit()
    
    def find_links(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM links WHERE trip_id = ? ''', (trip_id,)
        )
        
        links = cursor.fetchall()
        return links