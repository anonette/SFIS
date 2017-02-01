
var tech = require('./tech_vars.js');
var verbs = require('./verbs_vars.js');
var issues = require('./issues_vars.js');

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function choise(arr){
  var rndd = Math.floor(Math.random()*arr.length);
  return arr[rndd];
}

var i_tech = getRandomInt(0, tech.length)
var i_verbs = getRandomInt(0, verbs.length)
var i_issues = getRandomInt(0, issues.length)
console.log(i_tech,i_verbs,i_issues );
console.log(choise(tech[i_tech]),choise(verbs[i_verbs]),choise(issues[i_issues]) );