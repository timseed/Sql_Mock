import sqlite3


class People:

    def __init__(self):
        # DB File will be in Module's file location
        self.db_name = __file__.replace(".py",".db")

    def new(self):
        """
        :return: True ! Always !!
        """
        conn = sqlite3.connect(self.db_name)
        try:
            conn.execute("drop table phone")
        except Exception:
            print("Ignore exception")

        conn.execute("create table phone(name text, dial text)")
        print("Table created")
        data = [["tim", "123"],
                ["tsing", "456"],
                ["mike", "888"]]
        for rec in data:
            conn.execute("insert into phone(name,dial) values (?,?)", rec)
            print("Added")
        conn.commit()
        return True

    def query(self):
        conn = sqlite3.connect(self.db_name)
        return_data = [rec for rec in conn.execute("select name,dial from phone")]
        return return_data


if __name__ == "__main__":
    from pprint import pprint

    p = People()
    p.new()
    pprint(p.query())
