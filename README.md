# Ring-Theory



### Test Cases: 

- ##### Commutative Rings with Unity - 
```
mul_iden([0,1,2,3,4,5],6)
Unity = 1
```
```
mul_iden([0,2,4,6],8)
No Inverse
```

```
mul_iden([0,1,2,3,4,5,6,7],8)
Unity = 1
```

```
mul_iden([0,2,4],6)
Unity = 4
```

```
mul_iden([0,2,4,6,8],10)
Unity = 6
```

- ##### Multiplicatively invertible -


```
mult_invertible([0,1,2,3,4],5)
Unity = 1
Every element has a multiplicative inverse
```

```
mult_invertible([0,1,2,3,4,5],6)
Unity = 1
Not every non-zero element has a multiplicative inverse
```

```
mult_invertible([0,1,2],3)
Unity = 1
Every element has a multiplicative inverse
```

```
mult_invertible([0,1,2,3],4)
Unity = 1
Not every non-zero element has a multiplicative inverse
```

```
mult_invertible([0,2,4,6,8],10)
Unity = 6
Every element has a multiplicative inverse
```

- ##### Zero Divisors -

```
zero_divisors([0,1,2,3,4],5)
True for No Zero Divisors. 
No zero divisors exist so the given ring is an Integral domain
```

```
zero_divisors([0,1,2,3,4,5],6)
False for No Zero Divisors. 
Zero divisors exist so the given ring is not an integral domain
```

```
zero_divisors([0,1,2],3)
True for No Zero Divisors. 
No zero divisors exist so the given ring is an Integral domain
```

```
zero_divisors([0,1,2,3],4)
False for No Zero Divisors. 
Zero divisors exist so the given ring is not an integral domain
```

```
zero_divisors([0,2,4,6,8],10)
True for No Zero Divisors. 
No zero divisors exist so the given ring is an Integral domain
```
