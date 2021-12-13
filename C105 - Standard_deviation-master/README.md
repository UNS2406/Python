# Standard_deviation
solution for c105
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step

The formula for standard deviation (SD) is
\Large\text{SD} = \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu\rvert^2}}}{N}}SD= 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 start text, S, D, end text, equals, square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end square root
where \sum∑sum means "sum of", xxx is a value in the data set, \muμmu is the mean of the data set, and NNN is the number of data points in the population.
The standard deviation formula may look confusing, but it will make sense after we break it down. In the coming sections, we'll walk through a step-by-step interactive example. Here's a quick preview of the steps we're about to follow:
Step 1: Find the mean.
Step 2: For each data point, find the square of its distance to the mean.
Step 3: Sum the values from Step 2.
Step 4: Divide by the number of data points.
Step 5: Take the square root.
An important note
The formula above is for finding the standard deviation of a population. If you're dealing with a sample, you'll want to use a slightly different formula (below), which uses n-1n−1n, minus, 1 instead of NNN. The point of this article, however, is to familiarize you with the process of computing standard deviation, which is basically the same no matter which formula you use.
\text{SD}_\text{sample} = \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\bar{x}\rvert^2}}}{n-1}}SD 
sample
​
 = 
n−1
∑
​
 ∣x− 
x
ˉ
 ∣ 
2
 
​
 
​


Step-by-step interactive example for calculating standard deviation
First, we need a data set to work with. Let's pick something small so we don't get overwhelmed by the number of data points. Here's a good one:
6, 2, 3, 16,2,3,16, comma, 2, comma, 3, comma, 1
Step 1: Finding \goldD{\mu}μstart color #e07d10, mu, end color #e07d10 in \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\goldD{\mu}\rvert^2}}}{N}} 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, start color #e07d10, mu, end color #e07d10, close vertical bar, squared, divided by, N, end fraction, end square root
In this step, we find the mean of the data set, which is represented by the variable \muμmu.
Fill in the blank.
\mu =μ=mu, equals 
[Explain]
Step 2: Finding \goldD{\lvert x - \mu \rvert^2}∣x−μ∣ 
2
 start color #e07d10, open vertical bar, x, minus, mu, close vertical bar, squared, end color #e07d10 in \sqrt{\dfrac{\sum\limits_{}^{}{\goldD{{\lvert x-\mu}\rvert^2}}}{N}} 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, start color #e07d10, open vertical bar, x, minus, mu, close vertical bar, squared, end color #e07d10, divided by, N, end fraction, end square root
In this step, we find the distance from each data point to the mean (i.e., the deviations) and square each of those distances.
For example, the first data point is 666 and the mean is 333, so the distance between them is 333. Squaring this distance gives us 999.
Complete the table below.
Data point xxx	Square of the distance from the mean \lvert x - \mu \rvert^2∣x−μ∣ 
2
 open vertical bar, x, minus, mu, close vertical bar, squared
666	999
222	
333	
111	
[Explain]
Step 3: Finding \goldD{\sum\lvert x - \mu \rvert^2}∑∣x−μ∣ 
2
 start color #e07d10, sum, open vertical bar, x, minus, mu, close vertical bar, squared, end color #e07d10 in \sqrt{\dfrac{\goldD{\sum\limits_{}^{}{{\lvert x-\mu}\rvert^2}}}{N}} 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 square root of, start fraction, start color #e07d10, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, end color #e07d10, divided by, N, end fraction, end square root
The symbol \sum∑sum means "sum", so in this step we add up the four values we found in Step 2.
Fill in the blank.
\sum\lvert x - \mu \rvert^2 =∑∣x−μ∣ 
2
 =sum, open vertical bar, x, minus, mu, close vertical bar, squared, equals 
[Explain]
Step 4: Finding \goldD{\dfrac{\sum\lvert x - \mu \rvert^2}{N}} 
N
∑∣x−μ∣ 
2
 
​
 start color #e07d10, start fraction, sum, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end color #e07d10 in \sqrt{\goldD{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu}\rvert^2}}{N}}} 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 square root of, start color #e07d10, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end color #e07d10, end square root
In this step, we divide our result from Step 3 by the variable NNN, which is the number of data points.
Fill in the blank.
\dfrac{\sum\lvert x - \mu \rvert^2}{N} = 
N
∑∣x−μ∣ 
2
 
​
 =start fraction, sum, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, equals 
[Explain]
Step 5: Finding the standard deviation \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu\rvert^2}}}{N}} 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end square root
We're almost finished! Just take the square root of the answer from Step 4 and we're done.
Fill in the blank.
Round your answer to the nearest hundredth.
\text{SD} = \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu\rvert^2}}}{N}} \approxSD= 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 ≈start text, S, D, end text, equals, square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end square root, approximately equals 
[Explain]
Yes! We did it! We successfully calculated the standard deviation of a small data set.
Summary of what we did
We broke down the formula into five steps:
Step 1: Find the mean \muμmu.
\mu = \dfrac{6+2 + 3 + 1}{4} = \dfrac{12}{4} = \blueD3μ= 
4
6+2+3+1
​
 = 
4
12
​
 =3mu, equals, start fraction, 6, plus, 2, plus, 3, plus, 1, divided by, 4, end fraction, equals, start fraction, 12, divided by, 4, end fraction, equals, start color #11accd, 3, end color #11accd
Step 2: Find the square of the distance from each data point to the mean \lvert x-\mu\rvert^2∣x−μ∣ 
2
 open vertical bar, x, minus, mu, close vertical bar, squared.
xxx		\lvert x - \mu \rvert^2∣x−μ∣ 
2
 open vertical bar, x, minus, mu, close vertical bar, squared
666		\lvert6-\blueD{3}\rvert^2 = 3^2 = 9∣6−3∣ 
2
 =3 
2
 =9open vertical bar, 6, minus, start color #11accd, 3, end color #11accd, close vertical bar, squared, equals, 3, squared, equals, 9
222		\lvert2-\blueD{3}\rvert^2 = 1^2 = 1∣2−3∣ 
2
 =1 
2
 =1open vertical bar, 2, minus, start color #11accd, 3, end color #11accd, close vertical bar, squared, equals, 1, squared, equals, 1
333		\lvert3-\blueD{3}\rvert^2 = 0^2 = 0∣3−3∣ 
2
 =0 
2
 =0open vertical bar, 3, minus, start color #11accd, 3, end color #11accd, close vertical bar, squared, equals, 0, squared, equals, 0
111		\lvert1-\blueD{3}\rvert^2 = 2^2 = 4∣1−3∣ 
2
 =2 
2
 =4open vertical bar, 1, minus, start color #11accd, 3, end color #11accd, close vertical bar, squared, equals, 2, squared, equals, 4
Steps 3, 4, and 5:
\begin{aligned} \text{SD} &= \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu\rvert^2}}}{N}}\\\\\\\\ &= \sqrt{\dfrac{9 + 1 + 0 + 4}{4}} \\\\\\\\ &= \sqrt{\dfrac{{14}}{4}} ~~~~~~~~\small \text{Sum the squares of the distances (Step 3).} \\\\\\\\ &= \sqrt{{3.5}} ~~~~~~~~\small \text{Divide by the number of data points (Step 4).} \\\\\\\\ &\approx 1.87 ~~~~~~~~\small \text{Take the square root (Step 5).} \end{aligned} 
SD
​
  
= 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 
= 
4
9+1+0+4
​
 
​
 
= 
4
14
​
 
​
         Sum the squares of the distances (Step 3).
= 
3.5
​
         Divide by the number of data points (Step 4).
≈1.87        Take the square root (Step 5).
​
 
Try it yourself
Here's a reminder of the formula:
\Large\text{SD} = \sqrt{\dfrac{\sum\limits_{}^{}{{\lvert x-\mu\rvert^2}}}{N}}SD= 
N
∑
​
 ∣x−μ∣ 
2
 
​
 
​
 start text, S, D, end text, equals, square root of, start fraction, sum, start subscript, end subscript, start superscript, end superscript, open vertical bar, x, minus, mu, close vertical bar, squared, divided by, N, end fraction, end square root
And here's a data set:
1, 4, 7, 2,61,4,7,2,61, comma, 4, comma, 7, comma, 2, comma, 6
Find the standard deviation of the data set.
Round your answer to the nearest hundredth.
\text{SD}=SD=start text, S, D, end text, equals 
