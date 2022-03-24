const {MongoClient, ServerApiVersion} = require('mongodb');

async () => {


    // const client = await MongoClient.connect("mongodb+srv://matthewHoecker:Lays)Potato15963@cluster0.prjbu.mongodb.net/videoGame?retryWrites=true&w=majority", {useNewUrlParser: true, useUnifiedTopology: true});
    // const db = client.db("videoGame")

    // const items = await db.collections("enemyStats").fint({}).toArray();

    // console.log(items);

    // client.close();


    // connect to your cluster
    const client = await MongoClient.connect("mongodb+srv://matthewHoecker:Lays)Potato15963@cluster0.prjbu.mongodb.net/videoGame?retryWrites=true&w=majority", { 
        useNewUrlParser: true, 
        useUnifiedTopology: true,
    });
    // specify the DB's name
    const db = client.db('videoGame');
    // execute find query
    const items = await db.collection('enemyStats').find({}).toArray();
    console.log(items);
    // close connection
    client.close();
    // try{
    //     await client.connect();

    //     const findItem = await db.collections('enemyStats').find({}).toArray();

    //     console.log(`"Databases: ${findItem}"`);
    // } catch (e) {
    //     console.error(e);
    // } finally {
    //     await client.close();
    // }
}


// findItems().catch(console.error);

// async function showDatabases(client) {
//     const databaseList = await client.db(dbName).admin();

//     console.log("Databases:");
//     databaseList.listDatabases(function (Db, error){
//         console.log(`-${Db.name}`);
//     })
// }