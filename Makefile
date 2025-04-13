# Make sure they are all txts
.PHONY: txts
txts: make1.txt make2.txt

# Run both python files
make1.txt:
	python3 make1.py

make2.txt:
	python3 make2.py

# Final Clean Step
.PHONY: clean
clean:
	rm -f *.txt
