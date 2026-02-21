
let i=0;
let expences =[];
let o=0;
function addExpence(title,amount,category){

    let exp = {
        id:i,
        title:title,
        amount:amount,
        category:category,
    }
expences.push(exp)
i++;
}
function printAllExpenses(){
    console.log(expences)
}
function getTotalAmount(){
    for(let i2; i2<expences.length;i2++){
        o =o+expences[i](amount);
    }
        console.log(o);

}
function getExpensesByCategory(cat){
    let oy=0;
    for(let y=0; y<expences.length;y++){
        if(expences[y](category)==cat){
            oy =oy+ expences[y](amount);
            
        }
    }
    console.log(oy)
}
function findExpenseByTitle(titlee){
    for(let r=0; r<expences.length;r++)
        if(expences[r](title)=titlee){
            console.log(expences[r])
            r=expences.length;
        }

}
function IDdel(id){
    expences.splice(id,1)
    console.log(expences)
}


let expenseTracker= {
    mass:expences,
    exp:addExpence(),
    Totamt:getTotalAmount(),
    gEBC: getExpensesByCategory(),
    fEBT:findExpenseByTitle()
}

console.log("Выберите действие: 1-5")
let variant = prompt()
let f=0

if (variant===1){
    while(f<1){
    l=prompt()
    l2=prompt()
    l3=prompt()
    if(l.is.string(any)){
        if(l2.is.number(any)){
            if(l3.is.string(any)){
    
        addExpence(l,l2,l3)
        f=1
    }
    else{
        console.log("Неверный тип данных. Введите все данные заново")

    }
}else{
        console.log("Неверный тип данных. Введите все данные заново")

    }
}else{
        console.log("Неверный тип данных. Введите все данные заново")
}
    }
}
else if (variant===2){
    
        console.log(printAllExpenses())
    
}
else if (variant===3){
    l=prompt()
    if(l.is.string(any)){
        console.log(getExpensesByCategory(l))
    }else{
        console.log("Неверный тип данных. Введите все данные заново")
}
}
else if (variant===4){
    l=prompt()
    if(l.is.string(any)){
        console.log(findExpenseByTitle(l))
    }else{
        console.log("Неверный тип данных. Введите все данные заново")
}
}
else if (variant===5){
    l=prompt()
    if(l.is.number(any)){
        console.log(IDdel(l))
    }
}

