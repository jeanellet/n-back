clc;
clear all;
n = 3; %for n-back
base = 20; %%# of digits for 0-back task
result = zeros([2 base+n])
b_num = round(base*0.3);
flag = 0;

while flag == 0
    
    total = b_num*3;
    head = base+n - total;
    randloc = randi(3,1,b_num); %generate b_num 1-3 random numbers
    for i=1:b_num
        loc(i) = (i-1)*3+randloc(i)+head;% translate into exact location in the sequence
    end

    original = randi(10,1,base+n)-1;% generate base+n unrepeated random numbers
    new = original;
    for i = 1:b_num
        new(loc(i))= original(loc(i)-n);
    end
    result(1,:)=new;
    result(2,:)=0;
    for j=n+1:base+n
        if (result(1,j)==result(1,j-n))
           result(2,j)=1;
        end
    end
     one = length(find(result(2,:) == 1));
    if (one <= b_num+1 && one >= b_num)
        flag = 1;
        break
    end
end
result

