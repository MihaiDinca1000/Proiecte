"use strict";

var fs = require("fs");
var cowsay = require("cowsay");

var parsedArrayOfInts;
var despre = require("./package.json");
const setFunctions = new Set([
  "display",
  "addition",
  "subtraction",
  "division",
  "multiply",
  "modulo",
  "sqrt",
  "absolute",
  "power",
  "sort",
  "reverse",
  "maximum",
  "minimum",
  "unique",
  "sinus",
  "cosinus",
  ]);

function display() {
  console.log(cowsay.say({ text: "Calculator, Author: " + despre.author }));
  setFunctions.forEach(function(element) {
    console.log(element);
  });
}

function add(arr) {
  var sum = 0;
  arr.forEach(function(element) {
    sum += element;
  });
  return sum;
}





// function addC(rez,imz){
//   var sumr=0;
//   var sumi=0;

//   rez.forEach(function(element) {
//     sumr += element;
//   });
// }

//   imz.forEach(function(element) {
//     sumi += element;
//   });
// }





function sub(arr) {
  var dif = arr[0] * 2;
  arr.forEach(function(element) {
    dif -= element;
  });
  return dif;
}

function mul(arr) {
  var m = 1;
  arr.forEach(function(element) {
    m = m * element;
  });
  return m;
}

function div(arr) {
  var m = arr[0];
  arr.forEach(function(element, i) {
    if (i !== 0) m = m / element;
  });
  return m;
}

function sqrt(s1) {
  return Math.sqrt(s1);
}
function pow(p1, p2) {
  return Math.pow(p1, p2);
}

function abs(a1) {
  return Math.abs(a1);
}

function mod(m1, m2) {
  return m1 % m2;
}

function sor(arr) {
  arr.sort(function(a, b) {
    return a - b;
  });
  return arr
  .toString()
  .split(",")
  .join(" ");
}

function rev(arr) {
  return arr
  .reverse()
  .toString()
  .split(",")
  .join(" ");
}

function unq(arr) {
  return Array.from(new Set(arr))
  .toString()
  .split(",")
  .join(" ");
}

function max(ar) {
  let max = ar[0];
  for (let i = 1; i <= ar.length - 1; i++) {
    if (max < ar[i]) max = ar[i];
  }
  return max;
}

function min(ar) {
  let min = ar[0];
  for (let i = 1; i <= ar.length - 1; i++) {
    if (min > ar[i]) min = ar[i];
  }
  return min;
}

function sin(argument) {
  return Math.sin(argument);
}

function cos(argument) {
  return Math.cos(argument);
}



// function addComplex(arr) {
//   const firstRealArgument = 0;
//     const firstImaginaryArgument = firstRealArgument + 1;
//   const realSum = arr[firstRealArgument] + arr[firstRealArgument + 2];
//     const imaginarySum = arr[firstImaginaryArgument] + arr[firstImaginaryArgument + 2];
//     return `${realSum} + ${imaginarySum}i`;
// }

// function subtractComplex(arr) {
//   const firstRealArgument = 0;
//     const firstImaginaryArgument = firstRealArgument + 1;
//   const realSub = arr[firstRealArgument] - arr[firstRealArgument + 2];
//     const imaginarySub = arr[firstImaginaryArgument] - arr[firstImaginaryArgument + 2];
//     return `${realSub} - ${imaginarySub}i`;
// }

// function multiplyComplex(arr) {
//   const firstRealArgument = 0;
//     const firstImaginaryArgument = firstRealArgument + 1;
//   const realSub = arr[firstRealArgument] - arr[firstRealArgument + 2];
//     const imaginarySub = arr[firstImaginaryArgument] - arr[firstImaginaryArgument + 2];
//     return `${realSub} - ${imaginarySub}i`;
// }




function parseArguments() {
  const argumentPassed = process.argv[2];
  
  if (argumentPassed === "addition") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "addition");
    else console.log(add(parsedArrayOfInts));

  } else if (argumentPassed === "multiply") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "multiply");
    else console.log(mul(parsedArrayOfInts));

  } else if (argumentPassed === "sort") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 2) console.log("ERROR: %s command uses at least 1 parameters", "sort");
    else console.log(sor(parsedArrayOfInts));

  } else if (argumentPassed === "reverse") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 2) console.log("ERROR: %s command uses at least 1 parameters", "reverse");
    else console.log(rev(parsedArrayOfInts));

  } else if (argumentPassed === "subtraction") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "subtraction");
    else console.log(sub(parsedArrayOfInts));

  } else if (argumentPassed === "unique") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 2) console.log("ERROR: %s command uses at least 1 parameters", "unique");
    else console.log(unq(parsedArrayOfInts));

  } else if (argumentPassed === "division") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "division");
    else console.log(div(parsedArrayOfInts));

  } else if (argumentPassed === "display" || !argumentPassed) {
    display();

  } else if (argumentPassed === "sqrt") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    if (process.argv.length - 2 != 2) console.log("ERROR: %s command uses at least 1 parameters", "sqrt");
    else console.log(sqrt(firstArgIntVal));

  } else if (argumentPassed === "power") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    const secondArgIntVal = parseFloat(process.argv[4]);
    if (process.argv.length - 2 != 3) console.log("ERROR: %s command uses at least 2 parameters", "power");
    else console.log(pow(firstArgIntVal, secondArgIntVal));

  } else if (argumentPassed === "absolute") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    if (process.argv.length - 2 != 2) console.log("ERROR: %s command uses at least 1 parameters", "absolute");
    else console.log(abs(firstArgIntVal));

  } else if (argumentPassed === "modulo") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    const secondArgIntVal = parseFloat(process.argv[4]);
    if (process.argv.length - 2 != 3) console.log("ERROR: %s command uses at least 2 parameters", "modulo");
    else console.log(mod(firstArgIntVal, secondArgIntVal));

  } else if (argumentPassed === "minimum") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 2) console.log("ERROR: %s command uses at least 1 parameters", "minimum");
    else console.log(min(parsedArrayOfInts));

  } else if (argumentPassed === "maximum") {
    parsedArrayOfInts = [];
    for (let i = 3; i <= process.argv.length - 1; i++) {
      parsedArrayOfInts.push(parseFloat(process.argv[i]));
    }
    if (process.argv.length - 2 < 2) console.log("ERROR: %s command uses at least 1 parameters", "maximum");
    else console.log(max(parsedArrayOfInts));

  } else if (argumentPassed === "sinus") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    if (process.argv.length - 2 != 2) console.log("ERROR: %s command uses at least 1 parameters", "sinus");
    else console.log(sin(firstArgIntVal));

  } else if (argumentPassed === "cosinus") {
    const firstArgIntVal = parseFloat(process.argv[3]);
    if (process.argv.length - 2 != 2) console.log("ERROR: %s command uses at least 1 parameters", "cosinus");
    else console.log(cos(firstArgIntVal));


//complex

  // } else if (argumentPassed === "addComplex"){
  //       parsedArrayOfInts = [];
  //   for (let i = 3; i <= process.argv.length - 1; i++) {
  //     parsedArrayOfInts.push(parseInt(process.argv[i]));
  //   }
  //   // if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "addition");
  //   console.log(addComplex(parsedArrayOfInts));
  // }  else if (argumentPassed === "subtractComplex"){
  //       parsedArrayOfInts = [];
  //   for (let i = 3; i <= process.argv.length - 1; i++) {
  //     parsedArrayOfInts.push(parseInt(process.argv[i]));
  //   }
  //   // if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "addition");
  //   console.log(subtractComplex(parsedArrayOfInts));
  // }  else if (argumentPassed === "multiplyComplex"){
  //       parsedArrayOfInts = [];
  //   for (let i = 3; i <= process.argv.length - 1; i++) {
  //     parsedArrayOfInts.push(parseInt(process.argv[i]));
  //   }
  //   // if (process.argv.length - 2 < 3) console.log("ERROR: %s command uses at least 2 parameters", "addition");
  //   console.log(multiplyComplex(parsedArrayOfInts));

  } 
}

if (setFunctions.has(process.argv[2]) || process.argv.length === 2) {
  parseArguments();
} else {
  console.log("ERROR: this command does not exist, use display to see available commands");
}

// console.log("This prints a %s and a %d","string", 42);

// if (process.argv.length > 3 && process.argv[2] === "cos" ){
// 	console.log('restanta se plateste, se stie')
// }else { parseArguments(); }

// }else if (argumentPassed === "sqrt"){
// 	const firstArgIntVal =parseFloat(process.argv[3]);
// 	if(process.argv.length >4  !=undefined)
// 		console.log('ERROR: %s command uses at least 2 parameters','');
// 	else console.log(sqrt(firstArgIntVal));

// console.log(process.argv.length);
