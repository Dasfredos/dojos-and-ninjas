from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    DB = "dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id= data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        Ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninjas in results:
            Ninjas.append( cls(Ninjas) )
        return Ninjas

    @classmethod
    def save(cls, data ):
        query = """
                INSERT into ninjas
                (dojo_id, first_name, last_name, age)
                VALUES
                ( %(dojo_id)s ,%(first_name)s , %(last_name)s , %(age)s)
        """ 

        result = connectToMySQL(cls.DB).query_db(query,data)
        return result