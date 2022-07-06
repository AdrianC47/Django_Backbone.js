let inputValue = document.getElementById("personaID").value;
console.log(inputValue)
var PersonaModel = Backbone.Model.extend(
    
    //{
    // default:{
    //     id: 1, nombre: 'Luis sdf', apellido: 'Cabrera Bermeo', email: 'luiscabreraucme@hotmail.com', domicilio_id: 1
    // }
    //}
);

var PersonaCollection = Backbone.Collection.extend({
    // initialize: function(models, options){
    //     this.inputValue = options.inputValue
    // },
    model: PersonaModel,
    url:
    //  function() {return
     'http://127.0.0.1:8000/Listas/0' 
    //  + this.inputValue;
//}
});

var personaXD = new PersonaCollection();
// console.log(personaXD)
personaXD.fetch();
personaXD.toJSON();
var var1= Object.values(personaXD);
var var2 =var1[1];
var var3 =var2
// let dato;
// const tpl = personaXD.map(personaXD) 
// console.log(personaXD.models[0])
console.log(personaXD.models)
console.log(personaXD.models[0]);
// console.log(var1)
// console.log(var2)
// console.log(var3)
//  console.log(personaXD.models[0].attributes.Persona)
 

//  for (let i in personaXD){ 
   
//     for(let j in i ){
//        if(i=='models'){
//         console.log('uwu')
//         console.log(j)
//        }
  
        
//     }

//  }

//console.log(this.model)
// console.log(Object.values(personaXD).filter())
// console.log(JSON.stringify(personaXD.models.values))
// var hola = personaXD.models.values
// hola.json;
// console.log(hola)
// transformado = parseInt(inputValue)
// uwu.forEach(personavale => {
//     console.log(uwu.data)
//     // if(personavale.id ===transformado){
//     //     console.log(personavale);
//     //     console.log('sdfds')
//     // } else{
//     //     console.log('sdfds')
//     // }
// });
  

var PersonaView =  Backbone.View.extend({ 
    render: function(){
        this.$el.html(` 
            <div>Id Persona:`+`</div>
            <div>Nombre Persona:  </div>
            <div>Apellido Persona:  </div>
            <div>Email Persona:  </div>

    `)
        return this;
    }
     
});

var vista = new PersonaView({el:"#holi"});
vista.render();