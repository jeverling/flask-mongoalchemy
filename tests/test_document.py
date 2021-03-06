from tests import BaseAppTestCase
from nose.tools import assert_equals, assert_not_equals

class MongoAlchemyDocumentTestCase(BaseAppTestCase):
    "MongoAlchemy documents tests"

    def should_be_able_to_save_a_document_on_database_by_calling_its_save_method(self):
        "A document should be able to save itself in the database by calling it's \"save()\" method"
        todo = self.Todo(description=u'Reinvent the world')
        todo.save()
        assert_equals(self.Todo.query.count(), 1)

    def should_be_able_to_remove_a_document_on_database_by_calling_its_remove_method(self):
        "A document should be able to remove itself in the database by calling it's \"remove()\" method"
        todo = self.Todo(description=u'Reinvent the world')
        todo.save()
        assert_equals(self.Todo.query.count(), 1)
        todo.remove()
        assert_equals(self.Todo.query.count(), 0)

    def should_be_equal_by_the_id(self):
        "Two documents should be equal if they have the same mongo_id"
        todo = self.Todo(description=u'Reinvent the world')
        todo.save()
        my_new_todo = self.Todo(description=u'Save the world')
        my_new_todo.mongo_id = todo.mongo_id
        assert_equals(todo, my_new_todo)
        another_todo = self.Todo(description=u'Destroy the world')
        assert_not_equals(todo, another_todo)

    def should_be_able_update_a_document_by_calling_its_save_method(self):
        "A document should be able to update itself in the database by calling it's \"save()\" method"
        todo = self.Todo(description=u'Reinvent the world')
        todo.save()
        mongo_id = todo.mongo_id
        todo.description = u'Destroy the world.'
        todo.save()
        searched_todo = self.Todo.query.get(mongo_id)
        assert_equals(searched_todo.description, u'Destroy the world.')
        assert_equals(self.Todo.query.count(), 1)
