from titanic.model.dataset import Dataset
import pandas

class Service(object):
    dataset = Dataset()

    def new_model(self, payload: str) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        print(this.context + this.fname)
        return pandas.read_csv(this.context + this.fname, encoding='UTF-8')


def create_train(this: object) -> {}:
    return None


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