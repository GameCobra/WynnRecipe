function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function notMyFunction() {
    document.getElementById("demo").innerHTML = "Paragraph NOT changed.";
}

function Person(first = "a", last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
}

const TestPerson = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};

function newPerson()
{
    const mySelf = new Person(last="Too", age=22, eye="green");
    test = new CreateIngreadientObject();
    test.firstName = "jim";
    document.getElementById("demo").innerHTML = test.firstName;
}

function SolidUltravioletRay()
{
    const a = new CreateFullObject(3, 105, -175, 0);
    a.Weaponsmithing = true;
    a.Woodworking = true;
    a.Min.ManaRegen = 8;
    a.Max.ManaRegen = 10;
    a.Min.HealthRegenRaw = 90;
    a.Max.HealthRegenRaw = 100;
    a.Min.Intellegence = 5;
    a.Max.Intellegence = 5;
    a.Min.Defence = 5;
    a.Max.Defence = 5
    a.MinIntellegence = 30;
    a.MinDefence = 30;
    return a;

}

function CreateFullObject(stars, levelMin, durrability, durration)
{
    this.Stars = stars;
    this.LevelMin = levelMin;

    this.Durrability = durrability;
    this.Durration = durration;

    this.Weaponsmithing = false;
    this.Woodworking = false;
    this.Scribbing = false;
    this.Jewling = false;
    this.Alchemism = false;
    this.Cooking = false;
    this.Armouring = false;
    this.Tailoring = false;

    this.Min = new CreateStatsObject();
    this.Max = new CreateStatsObject();

    this.MinStrength = 0;
    this.MinIntellegence = 0;
    this.MinAgility = 0;
    this.MinDefence = 0;
    this.MinDexterity = 0;
}

function CreateStatsObject() 
{

    this.Earth = new CreateElementObject();
    this.Thunder = new CreateElementObject();
    this.Water = new CreateElementObject();
    this.Fire = new CreateElementObject();
    this.Air = new CreateElementObject();
    this.Neutral = new CreateElementObject();
    
    this.ElementalSpellDamage = 0;
    this.ElementalDamageBonusRaw = 0;
    this.ElementalDamagePercent = 0;
    this.RawElementalDamage = 0;
    this.RawElementalMainAttackDamage = 0;
    this.ElementalSpellDamagePercent = 0;
    this.ElementalDefence;

    this.Damage = 0;
    this.MainAttackDamage = 0;
    this.RawAttackSpeed = 0;
    this.RawMainAttackSpeed = 0;
    this.Poison = 0;

    this.SpellDamagePercent = 0;
    this.ManaSteal = 0;
    this.ManaRegen = 0;
    this.RawSpellDamage = 0;
    this.Raw1stSpellCost = 0;
    this.Raw2ndSpellCost = 0;
    this.Raw3edSpellCost = 0;
    this.Raw4thSpellCost = 0;
    this.S1stSpellCost = 0;
    this.S2ndSpellCost = 0;
    this.S3edSpellCost = 0;
    this.S4thSpellCost = 0;

    this.HealthRegenRaw = 0;
    this.LifeSteal = 0;
    this.Health = 0;
    this.HealthRegenPercent = 0;

    this.WalkSpeed = 0;
    this.SprintRegen = 0;
    this.JumpHeight = 0;
    this.Sprint = 0;

    this.LootBonus = 0;
    this.XPBonus = 0;
    this.Stealing = 0;
    this.LootQualty = 0;
    this.GatherXPBonus = 0;
    this.GatherSpeed = 0;

    this.Agility = 0;
    this.Defence = 0;
    this.Dexterity = 0;
    this.Strength = 0;
    this.Intellegence = 0;

    this.DamagePercent = 0;
    this.CriticalDamageBonus = 0;
    this.Exploding = 0;
    this.LeveledLootBonus = 0;
    this.LeveledXPBonus = 0;
    this.Reflection = 0;
    this.SlowEnemy = 0;
    this.Thorns = 0;
    this.WeakenEnemy = 0;

    this.GatheringSpeedBonus = 0;

}

function CreateElementObject() 
{
    this.strength = 0;
    this.Damage = 0;
    this.DamagePercent = 0;
    this.Defence = 0;
    this.SpellDamagePercent = 0;
    this.SpellDamage = 0;
}
