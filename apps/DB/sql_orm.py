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
        :param table: User
        :return:
        """
        all_data = self.db_session.query(table).all()
        res_list = []
        for i in all_data:
            # tmp_data = dict(zip(i.__dict__.keys(), i.__dict__.values()))
            tmp_data = i.__dict__
            tmp_data.pop('_sa_instance_state')
            res_list.append(tmp_data)
        return res_list

    def see_sql_sentence(self, table: str, filter=None or str) -> classmethod:
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

    def update_data(self, update_data_dict: dict) -> None:
        """
        :param update_one_data_dict:{"table": User, "filters": User.id == 1, "update_data": {'age': 'Mike','id':12}}
        :return: None
        """
        table, filters, update_data = update_data_dict.get("table"), update_data_dict.get("filters"), update_data_dict.get("update_data")
        self.db_session.query(table).filter(filters).update(update_data)
        self.db_session.commit()

        return None

    def update_data_add_str(self, update_data_dict: dict) -> None:
        """
        :param update_data_dict: {"table": User, "filters": User.id == 1, "update_data": {User.age: User.age + "626"}}
        :return: None
        """
        table, filters, update_data = update_data_dict.get("table"), update_data_dict.get("filters"), update_data_dict.get("update_data")
        self.db_session.query(table).filter(filters).update(update_data, synchronize_session=False)
        self.db_session.commit()
        return None

    def update_data_num_operate(self, update_data_dict: dict) -> None:
        """
        :param update_data_dict: {"table": User, "filters": User.id == 3, "update_data": {User.num: User.num - 12}}
        :return:
        """
        table, filters, update_data = update_data_dict.get("table"), update_data_dict.get("filters"), update_data_dict.get("update_data")
        self.db_session.query(table).filter(filters).update(update_data, synchronize_session="evaluate")
        self.db_session.commit()
        return None

    def delete_data(self, delete_data_dict: dict) -> None:
        """
        :param delete_data_dict:{"table": User, "filters": User.id == 1}
        :return: None
        """
        table, filters = delete_data_dict.get("table"), delete_data_dict.get("filters")
        self.db_session.query(table).filter(filters).delete()
        self.db_session.commit()
        return None

    def drop_db(self):
        """
        drop use111 table
        :return:
        """
        Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # 此处注释代码,单独测试使用,引入会有重叠字段,aa_one_str等等
    # add_one_str = User(name='one_data', age="19", num=123)
    # add_all_data_dict = {"table": User,
    #                      "add_all_data_list": [{'name': randint(1, 100), 'age': randint(1, 100)} for i in range(10000)]}
    OpOr = OperateOrm()
    # OpOr.add_one_data(add_one_str)
    # OpOr.add_all_data(add_all_data_dict)
    # OpOr.select_one_data(User, User.id >= 20)
    # OpOr.select_all_data(User)
    # OpOr.see_sql_sentence(User, User.id <= 20)

    # update_one_data_dict = {"table": User, "filters": User.id == 1, "update_data": {'name': "Jack"}}
    # OpOr.update_data(update_one_data_dict)

    # update_one_data_dict = {"table": User, "filters": User.id == 1, "update_data": {User.age: User.age + "626"}}
    # OpOr.update_data_add_str(update_one_data_dict)

    # update_one_data_dict = {"table": User, "filters": User.id == 3, "update_data": {User.num: User.num - 12}}
    # OpOr.update_data_num_operate(update_one_data_dict)

    # OpOr.drop_db()
