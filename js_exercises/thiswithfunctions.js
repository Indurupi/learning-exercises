var fullname = "john doe";
var obj = {
  fullname: "Colin irig",
  prop: {
    fullname: "aurelio de rosa",
    getFullname: function() {
      return this.fullname;
    }
  },
  getMyName: function() {
    return this.fullname
  },
  getFirstName: () => {
    return this.fullname.split(" ")[0];
  },
  getLastName: (function() {
    return this.fullname.split(" ")[1];
  })(),
  getLastName2: (() => {
    return this.fullName.split(' ')[1];
  })()
}

console.log(obj.prop.getFullname());
console.log(obj.getFirstName());
console.log(obj.getMyName());
console.log(obj.getLastName);
console.log(obj.getLastName2);