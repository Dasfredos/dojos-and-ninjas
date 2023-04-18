from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninjas import Ninjas


class Dojos:
    DB = "dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []
    # Now we use class methods to query our database
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for all_dojos in results:
            dojos.append( cls(all_dojos) )
        return dojos

    @classmethod
    def dojo_with_ninjas(cls, data):
        query= '''
            SELECT * FROM dojos
            LEFT JOIN ninjas
            ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        '''
        results= connectToMySQL(cls.DB).query_db(query, data)
        print (results)
        # creating a User instance from the database info of the user
        dojo = cls(results[0])
        for row in results:

            # parsing out the database data for the post
            ninja_data={
                "id" : row['ninjas.id'],
                "dojo_id" : row['dojo_id'],
                "first_name": row['first_name'],
                "last_name":row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }

            # creating a post instance and appending it to the user's all_post attribute-which is an empty list.
            dojo.all_ninjas.append(Ninjas(ninja_data))

            # return this user to the route in the controller, to be used in the template
        return dojo





    @classmethod
    def save_dojo(cls, data ):
        query = """
                INSERT into dojos
                (name)
                VALUES
                ( %(name)s);
        """ 
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results