#!/bin/sh
cd papers
for paper in *.pdf
do
  pdftotext $paper 
done

cat *.txt > all_papers.text
