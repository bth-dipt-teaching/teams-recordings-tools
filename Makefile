.PHONY: test

test:
	@echo -n Test clean_vtt.py ...
	@cat test/input.vtt | python clean_vtt.py | diff test/output_clean.vtt - && echo " OK"
	@echo -n Test offset_vtt.py ...
	@cat test/input.vtt | python offset_vtt.py 12.5 | diff test/output_offset.vtt - && echo " OK"
