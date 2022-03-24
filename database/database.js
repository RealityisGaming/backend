const {MongoClient, ServerApiVersion} = require('mongodb');
const dbName = 'videoGame'

const findItems = async function main() {

    const uri ="mongodb+srv://matthewHoecker:Lays)Potato15963@cluster0.prjbu.mongodb.net/videoGame?retryWrites=true&w=majority";

    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });
    try {
        await client.connect();

        createUser(client, {
            email: "",
            password: ''
        })

    } catch (e) {
        console.error(e);
        client.close();   
    }
}


findItems().catch(console.error);

async function createUser(client, newUser) {
    const result = await client.db("users").collection('userLogin').insertOne(newUser);

    console.log(`Check it ${result.insertedId}`)
}

async function showDatabases(client) {
    const databaseList = await client.db(dbName).admin();

    console.log("Databases:");
    databaseList.listDatabases(function (Db, error){
        console.log(`-${Db.name}`);
    })
}