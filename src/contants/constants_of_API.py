
class Constant_portion:

#Constant portion of Url
    @staticmethod
    def url_portion():
        return "https://petstore.swagger.io/v2/"
class Setion_portion(Constant_portion):
#Constant of Pet to Add and update
    @staticmethod
    def url_pet():
        urlp= Setion_portion.url_portion() + "pet"
        return urlp

#Constant of Store
    @staticmethod
    def url_store():
        urls= Setion_portion.url_portion() + "store"
        return urls
#Constant of User to create and rest API
    @staticmethod
    def url_user():
        urlu= Setion_portion.url_portion() + "user"
        return urlu

class Pet:
#Pet Image upload
    @staticmethod
    def upload_image(petId):
        ulimag=Setion_portion.url_pet() + f"/{petId}/uploadImage"
        return ulimag

#Get pet by status available,sold,pending
    @staticmethod
    def find_by_status(status):
        return Setion_portion.url_pet() + f"/findByStatus?status={status}"

#Get pet by Tag
    @staticmethod
    def find_by_tag(tags):
        return Setion_portion.url_pet() + f"/findByTags?tags={tags}"
#Get,Update,Delete by ID
    @staticmethod
    def find_update_delete_by_petId(petId):
        return Setion_portion.url_pet() + f"/{petId}"

class Store:
#Create Order
    @staticmethod
    def create_order():
        return Setion_portion.url_store() + "/order"

#Get Delete Order
    @staticmethod
    def find_delete_order_id(orderId):
        return Setion_portion.url_store() + f"/order/{orderId}"

#Get Inventory count
    @staticmethod
    def inventory():
        return Setion_portion.url_store() + "/inventory"

class User:

#Create multiple users together
    @staticmethod
    def create_withlist():
        return Setion_portion.url_user() + "/createWithList"
#Get, Update,Delete user by username
    @staticmethod
    def get_update_delete_by_username(username):
        return Setion_portion.url_user() + f"/{username}"

#Login
    @staticmethod
    def user_login(username,password):
        return Setion_portion.url_user() + f"/login?username={username}&password={password}"

#Logout
    @staticmethod
    def user_logout():
        return Setion_portion.url_user() + "/logout"






