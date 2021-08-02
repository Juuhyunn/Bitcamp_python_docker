from titanic.model.dataset import Dataset
import pandas as pd

class TitanicService(object):
    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = '../titanic/data/'
        this.fname = payload
        print(this.context + this.fname)
        return pd.read_csv(this.context + this.fname + '.csv', encoding='UTF-8')

    def count_survived_dead(self) -> []:
        return []

    # def create_train(this: object) -> {}:
    #     return None


    def create_label(this: object) -> {}:
        return None


    def drop_feature(this: object, *feature) -> object:
        return this


    def embarked_nominal(this: object) -> object:
        return this


    def fare_ordinal(this: object) -> object:
        return this


    def title_nominal(this: object) -> object:
        return this


    def gender_nominal(this: object) -> object:
        return this


    def age_nominal(this: object) -> object:
        return this


    def create_k_fold() -> {}:
        return None


    def accuracy_by_classfier(this: object) -> str:
        return ""