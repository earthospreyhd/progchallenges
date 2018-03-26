def binsearch (targ, input, inputlen):

    sortin = sorted(input);

    found = False;

    offset = 0;

    while (not found):

    	middle = int (len(sortin) / 2);

	if (sortin[middle] == targ):

            found = True;

            offset += middle;

            break;


	if (targ > sortin[middle]):

	    sortin = sortin[middle:inputlen];

            offset += middle;
	
	else:
            
            sortin = sortin[0:middle];
            
    return offset + 1;

input = [1,4,4,7,7,8,11,19,21,23,24,30];

print binsearch(23,input, len(input));
