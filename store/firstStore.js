console.clear();
let itemArray = []
let currency = 265

const Store = () => {
    console.clear();
    const itemOne = takeUserOrder();
    itemOne.setItem();
    
    const itemTwo = takeUserOrder();
    itemTwo.setItem();
    
    const itemThree = takeUserOrder();
    itemThree.setItem();
  
    const itemFour = takeUserOrder();
    itemThree.setItem();
    
};


const takeUserOrder = () => {
    let userType, userFoodItem;

    const viewMenu = prompt('Healing, Antidotes and Gear')

    switch(viewMenu) {
        case 'Healing':
            alert('For healing we have potion, repotion and megapotion');
            userType = 'healing'
            userFoodItem = prompt(`Take your pick from our ${userType} menu.`);

            break;

        case 'Antidotes':
            alert('For antidotes we have antidote, hiantidote, and megantidote');
            userType = 'antidotes';
            userFoodItem = prompt(`Pick your posion from ${userType} menu`);

            break;

        case 'Gear':
            alert('For gear we have leather, steel, robes, daggers, swords, and staffs')
            userType = 'gear';
            userFoodItem = prompt(`What you want from ${userType} menu?`)

            break;
    }
    const menu = new menuItem(userType, userFoodItem)
    return menu
};




class menuItem{
    constructor(type, userChoice){
        this.type = type,
        this.userChoice = userChoice
      }
    setItem(){
        const healing = {
            potion: 15,
            repotion: 25,
            megapotion: 50,
        };

        const antidotes = {
            antidote: 20,
            hiantidote: 35,
            megantidote: 70
        };

        const gear = {
            dagger: 80,
            staff: 75,
            sword: 100,
            leather: 75,
            robes: 75,
            steel: 115
        };


        if(this.type === 'healing'){
            this.menu = healing;
        } else if(this.type === 'antidotes'){
            this.menu = antidotes
        } else if (this.type === 'gear'){
            this.menu = gear
        } 

        this.price = this.menu[this.userChoice];
        itemArray.push(this.price)
        const reducer = (total, element) => total + element;
        let totalItemPrice = itemArray.reduce(reducer)
        let quantity = prompt('How many would you like?');
        let total = this.price * quantity;
        // let newTotal = total
      console.log(totalItemPrice);
      console.log(total)
        let newQuantity = quantity > 1 ? total : totalItemPrice;
        let currentCurrency = currency - newQuantity;
      console.log(currency);
      console.log(currentCurrency);
      
        if(currency >= total) {
        console.log(`Your wallet consists of ${currentCurrency}`)
        } else {
        console.log("What ya broke?")
      };
    }

};



Store();