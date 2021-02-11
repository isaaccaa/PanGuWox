# -*- coding: utf-8 -*-
from util import WoxEx, WoxAPI, load_module, Log
import pyperclip
import pangu


class Main(WoxEx):  # 继承WoxEx
    def query(self, keyword):
        results = list()
        results.append({
            "Title": "input",
            "SubTitle": keyword,
            "IcoPath": "Images//app.png",
            "JsonRPCAction": {
                "method": "pangu_func",
                "parameters": [keyword],
                "dontHideAfterAction": False
            }
        })
        return results

    def pangu_func(self, keyword):
        text = pyperclip.paste()
        new_text = pangu.spacing_text(text)
        pyperclip.copy(new_text)

if __name__ == "__main__":
    Main()
    