'''
logical gates :Logic gates are elementary building blocks for any digital circuits.
It takes one or two inputs and produces output based on those inputs. Outputs may be high (1) or low (0)

AND gate : The AND gate gives an output of 1 if both the two inputs are 1, it gives 0 otherwise
 example:  1 and 1  =>  1   True and True   => True
            1 and 0  =>  0   True and False  => False
             0 and 1  =>  0   False and True  => False
                0 and 0  =>  0   False and False => False

OR gate :    The OR gate gives an output of 1 if either of the two inputs are 1, it gives 0 otherwise
 example :    1 or 1  =>  1   True or True   => True
                1 or 0  =>  1   True or False  => True
                   0 or 1  =>  1   False or True  => True
                        0 or 0  =>  0   False or False => False

NOT gate :  It acts as an inverter. It takes only one input.
If the input is given as 1, it will invert the result as 0 and vice-versa

 example : not 1 =>  0       not True  => False
           not 0 =>  1       not False => True

      1s compliment ==     one's compliment operator will invert the binary bits
                  If a bit is 1, it will change it to 0.
                If the bit is 0, it will change it to 1
                example : 1101110 ==> 0010001
    2s compliment ==        1's complement of given number plus 1 to the least significant bit (LSB)
                        example : 1s + 1 => 0010001
                                                 1

                                      ==>      0010010
