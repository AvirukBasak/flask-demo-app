## Flask Matrix API
An endpoint requires some URL parameters.
Some may require only 1, while others may require 2.

Some URL parameters may be numeric, while others may be matrices.

#### Usage
- `pip install -r requirements.txt`
- `python app.py`

#### Type based on parameter name
- `A`: Matrix; used as first parameter
- `B`: Matrix; used as second parameter
- `k`: Numeric; int or float

#### Endpoints
- `/api/add`: requires `A` and `B`: sum
- `/api/sub`: requires `A` and `B`: difference
- `/api/mul`: requires `A` and `B`: product
- `/api/mul`: requires `A` and `k`: scaling
- `/api/pow`: requires `A` and `k`: power
- `/api/det`: requires `A`: determinant
- `/api/trn`: requires `A`: transpose
- `/api/adj`: requires `A`: adjoint
- `/api/inv`: requires `A`: inverse

#### Example
- [`/api/det?A=[[1,3,4],[2,4,6],[7,6,8]]`](/api/det?A=[[1,3,4],[2,4,6],[7,6,8]])
- [`/api/mul?A=[[1,0,0],[0,1,0],[0,0,1]]&k=6`](/api/mul?A=[[1,0,0],[0,1,0],[0,0,1]]&k=6)


Note how the syntax to pass a matrix is same as python syntax.

This is made possible by passing the parameter into `eval`.
This should open all sorts of security issues, so it'll be interesting.

Also note, even if some characters may be invalid in a parameter, modern browsers should automatically URL encode the data.
