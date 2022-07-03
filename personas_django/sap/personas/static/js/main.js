var PersonaModel = Backbone.Model.extend();

var PersonaCollection = Backbone.Collection.extend({
    model: PersonaModel,
    url: 'Listar_Persona'
});

var persona = new PersonaCollection();

var PersonaView = Backbone.View.extend({
});
