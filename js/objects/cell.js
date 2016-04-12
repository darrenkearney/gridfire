function Cell(kwargs) {

    if (!kwargs) {
        kwargs = {};
    }

    this.name =     kwargs.name     || 'Cell';
    this.desc =     kwargs.desc     || 'Contains data about a point on a grid';  
    this.coord =    kwargs.coord    || [0,0];
    this.visited =  kwargs.visited  || 'false';   

    for (var k in kwargs) {
        if (kwargs.hasOwnProperty(k)) {
            this[k] = kwargs[k] || '';
        }
    }

    this.testMethod =   function () {
        console.log("testMethod called");
    }
}

Cell.prototype.getInfo = function () {
    return this.name + ', coord: ' + this.coord + ', visited: ' + this.visited;
}

Cell.prototype.__init__