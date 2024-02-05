all: PersianandKoreanBussiness.pdf
	echo "everything has been built"

#clean:
#	rm PersianandKoreanBusiness.pdf prod3.txt prod2.txt prod1.txt

#graphing the plot 
PersianandKoreanBussiness.pdf: prod3.txt 
	python3 plot.py 

#for each zip code getting the Persian ratio, Korean ratio, corp ratio
prod3.txt: prod3.py prod2.txt prod1.txt
	python3 ./prod3.py > prod3.txt

#for each zip code getting #Persians, #Koreans, totalPop
prod2.txt:prod2.py acs.gz
	python3 ./prod2.py > prod2.txt

#for each zip code getting the # of new corps from past 5 years 
prod1.txt: prod1.py corp.gz
	python3 ./prod1.py > prod1.txt
