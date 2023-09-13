from abstracts_class import FileVacancy
import json
import os
from typing import List, Dict, Any

class JSON_File(FileVacancy):
    def save(self, vacancy_data: List[Dict[str, Any]]) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding="utf-8") as f:
                data_list = json.load(f)
            with open(self.file_path, 'w', encoding="utf-8") as f:
                data_list += vacancy_data
                json.dump(data_list, f, indent=2, ensure_ascii=False)
                f.write('\n')
        else:
            with open(self.file_path, 'w', encoding="utf-8") as f:
                json.dump(vacancy_data, f, indent=2, ensure_ascii=False)
                f.write('\n')

    def get_by_name(self, name: str) -> None:
        with open(self.file_path, 'r', encoding="utf-8") as f:
            data_list = json.load(f)
            for data in data_list:
                if name in data['name']:
                    print(data)

    def del_by_id(self, id: int) -> None:
        with open(self.file_path, 'r', encoding="utf-8") as f:
            data_list = json.load(f)
        with open(self.file_path, 'w', encoding="utf-8") as f:
            data_list_new = []
            for data_item in data_list:
                if data_item['id'] != id:
                    data_list_new.append(data_item)
            json.dump(data_list_new, f, indent=2, ensure_ascii=False)
            f.write('\n')
