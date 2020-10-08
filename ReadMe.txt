08/10/2020:
    9PM: Main work:
        * implement relative, k-means grading and compare them and share insights
        * tips = gaps finding and gaps dealing.


    Points:
        * get relative rule and assign grades.
        * the problem will be in gaps.
        * find gaps heuristic function or DBI formula
        * apply to evaluate

        * find kmeans algo
        * apply kmeans algo for grades
        * evaluate clustering quality

        * show results to sir.

        * do literature review of last research paper. 

13/09/2020:
    Problem
    1. get an excel sheet
    2. convert marks to grades
    3. apply different techniques

    There is a text file with input policy, how many to assign A grades, min limit, max limit, min %, max % 
    and same for all other grades. A simple setting, a complex settings below.

    Done:
    1. implemented grade_absolute()
    2. implemented graph on excel spread sheet.
    2. added git

02/10/2020:
    Problem:
    1. shayan, muneeb algo:
    max marks (93->100%)
    make peecentiles
    outliers nikal dein (upper, lower)
    normal-distr rank
    apply k-means


    muneeb:
    tree of different tech...

7 Oct 2020:
    10PM:
        Progress:
        I did some coding in python. I was trying to implement relative grading. Python skills were weak. So I will revise python in Sololearn app and code tomorrow IA.
        
        Thoughts:
        0.  Sort on excel sheet. X concept in softdev.

        I = No grade 
        I want to apply these features. Now.
        1. grades_relative(marks_list, rule) #marks the list with grades.

        1. grades_relative(
            marks_list = [[20, 'I'], [35, 'I'], [80, 'I'], [50, 'I'], [30, 'I']],
                   
            rule = [[5,'A+'], [5,'A'], [5,'A-'], 
                    [10,'B+'], [10,'B'], [10,'B-'], 
                    [10,'C+'], [10,'C'], [10,'C-'], 
                    [10,'D+'], [5,'D'], [5,'D-'],
                    [5,'F']])
        Later:
        1. grades_kmeans(marks_list, rule)
        grades_kmeans(marks_list, clusters = 10, grades = [A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F])

        Later On:
        Load grades, rule from excel sheet or txt file.




#Reference Code:
def sort_marks_column(filename):
    data = np.array([[5,2], [4,1], [3,6]])
    data = data[data[:,0].argsort()]  # sort on column 0
    print('data:')
    print(data)