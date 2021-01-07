# !/bin/env python
# -*- coding=utf-8 -*-
from random import randint
from apps.DB.database.model import *
from sqlalchemy.orm import sessionmaker


class OperateOrm(object):
    def __init__(self):
        self.engine = engine
        self.session = sessionmaker(engine)
        self.db_session = self.session()

    def add_one_data(self, add_one_str: str) -> None:
        """
        :param filter:  User(name="john005", age="12313123")
        :return: None
        """
        self.db_session.add(add_one_str)
        self.db_session.commit()
        self.db_session.close()
        print("add one data")

    def add_all_data(self, add_all_data_dict: dict) -> None:
        """
        :param add_data_dict:  {"table": User,
                                "add_all_data_list":[{'name': 59, 'age': 82}, {'name': 2, 'age': 100}]}
        :return: None
        """
        table, add_data_list = add_all_data_dict.get("table"), add_all_data_dict.get("add_all_data_list")
        self.db_session.execute(table.__table__.insert(), add_data_list)
        self.db_session.commit()
        print("add some data")

    def select_one_data(self, table: str, filter: str) -> dict or None:
        """
        :param table: User
        :param filter: User.id >= 20
        :return:
        """
        user = self.db_session.query(table).filter(filter).first()
        if user is None:
            return None
        else:
            print(user.id, user.name)
        self.db_session.close()

    def select_all_data(self, table: str) -> list:
        """
        ORM to  list
        :param table:
        :return:
        """
        all_data = self.db_session.query(table).all()
        res_list = []
        for i in all_data:
            tmp_data = dict(zip(i.__dict__.keys(), i.__dict__.values()))
            tmp_data.pop('_sa_instance_state')
            res_list.append(tmp_data)
        return res_list

    def see_sql_sentence(self, table: str, filter=None) -> classmethod:
        """
        :param table: USER
        :param filter: User.id >= 20  or  None
        :return: SELECT user.id AS user_id, user.name AS user_name  FROM user  WHERE user.id >= ?
        """
        if filter is not None:
            res = self.db_session.query(table).filter(filter)
            return res
        else:
            res = self.db_session.query(table)
            return res

    def drop_db(self):
        """
        drop use111 table
        :return:
        """
        Base.metadata.drop_all(engine)


if __name__ == '__main__':

    add_one_str = User(name='one_data', age="19")
    add_all_data_dict = {"table": User,
                         "add_all_data_list": [{'name': randint(1, 100), 'age': randint(1, 100)} for i in range(10000)]}
    OpOr = OperateOrm()
    # OpOr.add_one_data(add_one_str)
    # OpOr.add_all_data(add_all_data_dict)
    # OpOr.select_one_data(User, User.id >= 20)
    # OpOr.select_all_data(User)
    # OpOr.see_sql_sentence(User, User.id <= 20)
    # OpOr.drop_db()
