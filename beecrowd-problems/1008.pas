// Solution of: https://www.beecrowd.com.br/judge/problems/view/1008 Language: Pascal

var
    number: integer;
    hours: integer;
    salhour: real;
    salary: real;
begin
    read(number);
    read(hours);
    read(salhour);
    
    salary := hours * salhour;
    
    Writeln('NUMBER = ', number);
    Writeln('SALARY = U$ ', salary:0:2);
end.
