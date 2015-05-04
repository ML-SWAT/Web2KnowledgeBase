matrix_file='/Users/JudeWang/Documents/Web2KnowledgeBase/CoTrade/matrix1.csv';
M = csvread(matrix_file);
% size(M);%1051*18871

matrix_file2='/Users/JudeWang/Documents/Web2KnowledgeBase/CoTrade/matrix2.csv';
M2 = csvread(matrix_file2);


Learner.type='NB'; % Suppose we use Naive Bayes as the base learner
Learner.attri_type=0; % Binary features for the experimental data

train_course_number=5;
train_non_course_number=5;
test_number = 100;
r_course = randi([1 230],1,train_course_number);
r_non_course = randi([231 1051-231],1,train_non_course_number);
r_course;%50 162 74 163 179
r_non_course;%522 250 597 358 249

r_train = [r_course r_non_course];
L_data1 = M(r_train,:);
L_data2 = M2(r_train,:);
M(r_train,:)=[];
M2(r_train,:)=[];
size(M);
L_target=[1;1;1;1;1;0;0;0;0;0];

r_test = randi([1,size(M,1)],1,100);
Test_data1 = M(r_test,:);
Test_data2 = M2(r_test,:);
Test_target = (r_test<231-sum(r_train<231));
M(r_test,:)=[];
M2(r_test,:)=[];

U_data1 = M;
U_data2 = M2;

Max_iter=50;
Accuracy=CoTrade(Learner,L_data1,L_data2,U_data1,U_data2,L_target,Test_data1,Test_data2,Test_target,Max_iter);

