class Hero {
    constructor({ race, job, backGround, level = 1}){
        this.race = race;
        this.job = job;
        this.backGround = backGround;
        this.level = level;
    }
    
    renderHero(){
        console.log(1`
        Race: ${this.race}\n
        Class: ${this.job}\n
        Past: ${this.backGround}\n
        Level: ${this.level}`)
    }
}

const warrior = new Hero(Object.values(race = 'Human'), Object.values(job = 'Warrior'), Object.values(backGround = 'Royal'), Object.values(level = 1) )
const thief = new Hero(Object.values(race = 'Dwarf'), Object.values(job = 'Thief'), Object.values(backGround = 'Commoner'), Object.values(level = 1) )
const mage = new Hero(Object.values(race = 'Elf'), Object.values(job = 'Mage'), Object.values(backGround = 'Wood Elf'), Object.values(level = 1) )
// Dwarf Human Elf

// Royals Commoners 
// Royals Commoners

// Wood elves High elves 

console.log(warrior)
console.log(thief)
console.log(mage)