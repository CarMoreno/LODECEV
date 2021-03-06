#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rdflib import Namespace, URIRef, Literal, Graph
from ontologias import UMBEL, CRUZAR, GEOES
from rdflib.namespace import RDF, RDFS, FOAF
from inicio import g, dbr

rutaMaiz = Namespace('http://190.14.254.237/dataseteco/RutaDelMaiz/')

g.add( (URIRef(rutaMaiz), GEOES.formaParteDe, dbr.Tulua))
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Alojamientos ) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Empresas) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Eventos) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Fauna) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Flora) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Lugares) )
g.add( (URIRef(rutaMaiz), UMBEL.hasCharacteristic, rutaMaiz.Restaurantes) )
g.add( (URIRef(rutaMaiz), RDF.type, CRUZAR['Recurso-turistico']))

g.add( (URIRef(rutaMaiz), RDFS.label, Literal("Ruta del Maíz")) )
g.add( (URIRef(rutaMaiz), RDFS.comment, Literal("""Es una ruta de alto valor paisajístico, donde 
    el turista podrá deleitarse con la variedad de cultivos de cítricos, cultivos de maíz, cultivos de flores 
    exóticas. Comprende las gastronomía en torno de los productos a base de maíz, tales como trasnochados, 
    cuaresmeros, pandebonos, tortas, envueltos, masato, champús, chancarina y otros. El recorrido comienza desde 
    el Parque Carlos Sarmienta Lora, atravesando toda la ciudad de Tuluá hasta llegar al corregimiento de Campoalegre.""")) )
g.add( (URIRef(rutaMaiz), FOAF.depiction, URIRef("https://www.google.com/maps/d/embed?mid=z6wVQXo7qC0A.kYZp_Mzxz-Gg")) )

#print (g.serialize(format='pretty-xml'))	
