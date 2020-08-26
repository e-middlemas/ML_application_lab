# Intro to Machine Learning Application Lab
### For CU-Boulder's ATOC and University of Wisconsin's Objective Data Analysis course

1. Download zip or checkout repository
2. Navigate to the directory containing the application lab
3. Execute in terminal `conda env create -f environment.yml`
4. Then, activate the environment by running `conda activate intro2ml`. 
5. Execute `python -m ipykernel install --user --name intro2ml` to ensure jupyter-lab can access your environment. *One should re-run this line if any changes to the environment are made.*
6. Open jupyter-notebooks or jupyter-lab
7. Start with the unsupervised learning notebook. 
8. Finish with the supervised learning notebook. *Note: There's a chance tensorflow won't import correctly. In that case, navigate back to your terminal, ensure the `intro2ml` environment is activated and enter:* `python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.3.0-cp37-cp37m-macosx_10_9_x86_64.whl`. Then re-perform step #5 above.
9. Have fun!
