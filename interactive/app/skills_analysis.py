degrees = {'masters': 'master', 'master': 'master', 'masc': 'master', 'meng': 'master', 'ms': 'master',\
           'phd': 'phd', 'doctor': 'phd',\
           'bachelor': 'bachelor', 'btech': 'bachelor', 'bs': 'bachelor'}

skills_type = {'acumendesign': 'visualization', 'python':'python', 'sql':'sql', 'excel':'excel', 'java':'java', 'c':'c', 'c+': 'c+', 'c++': 'c++', 'r': 'r', 'tableau': 'visaulization',
               'spark':'big data', 'hadoop':'big data', 'm': 'sql', 'azure': 'cloud', 'tensorflow': 'framework', 'acumen': 'visualization','design': 'analytics',\
               'sap': 'framework', 'd3': 'visualization', 'cloud': 'cloud', 'data mining': 'big data', 'creating algorithms': 'ml','data manipulation': 'big data', \
               'data wrangling': 'big data', 'big data':'big data', 'api': 'cloud', 'apiengine':'cloud', 'aws': 'visualization', 'dplyr': 'sql', \
               'information retrieval':'big data', 'interpreting data':'big data', 'keras':'framework', 'mathematics': 'statistics', 'statistics':'statistics',\
               'matlab':'matlab', 'excel':'excel', 'predictive models':'ml', 'machine learning':'ml', 'recommendation engines':'analytics', \
               'reinforcement learning':'deep learning', 'risk modeling':'simulation', 'scripting languages':'ml', 'speech recognition':'ml',\
               'statistical learning models':'probability model', 'statistical modeling':'probability model', 'supervised':'ml',\
               'unsupervised':'ml', 'simulation':'simulation', 'tensorflow':'framework', 'time series':'time series', \
               'nlp':'ml', 'logistic':'ml', 'linear':'ml', 'optimization':'optimization', 'mathematical modelling':'probability model', \
               'matplotlib':'visualization', 'neural networks':'deep learning', 'nltk':'framework', 'numpy':'framework', 'pandas':'framework', \
               'random forests':'ensemble method', 'deep learning':'deep learning', 'seaborn':'visualization', 'sklearn':'framework', \
               'ensemble methods':'ensemble method', 'knn':'ml', 'naives bayes':'ml', 'svm':'ml',\
               'hypothesis testing':'statistics', 'decision trees':'ml', 'web scraping':'analytics', 'chatbots':'analytics',\
               'network analysis':'deep learning', 'bokeh':'visualization', 'cluster analysis':'ml', \
               'gradient boosting':'ensemble method', 'principle component analysis':'ml', 'build pipeline':'automated tools','feature engineering':'analytics', \
               'monte carlo':'simulation', 'hyperparameter tuning':'ml', 'model validation':'ml', 'ggplot':'visualization', 'plotly':'visualization',\
               'geoplotlib':'visualization', 'tableau':'visualization', 'model training':'ml', \
               'model testing':'ml', 'relational Database':'sql', 'pyspark':'big data', 'query tuning':'sql', 'error handling':'sql',\
               'recursive queries':'sql', 'postgresql':'sql', 'triggers':'sql', 'neural nets':'deep learning', 'tensors':'python', 'kafka':'framework', 'pivot tables':'excel', 'multivariable calculus':'statistics', \
               'nosql':'sql', 'scikit':'framework', 'scipy':'framework', 'xgboost':'ensemble', 'validating analytics:':'analytics', 'Gradient Bossting Machines': 'ensemble',\
               'Carcet': 'framework', 'Caret': 'framework', 'Bash': 'scripting', 'Keras': 'framework', 'SQL': 'sql', 'Automated Hypreparameter Tuning': 'automated tools', 'Dense NNs': 'deep learning',\
               'D3.js': 'visualization', 'Spark MLib': 'big data','MATLAB': 'matlab','CNN': 'deep learning', 'Automated Full ML Pipelines': 'automated tools',\
               'RNN': 'deep learning', 'Bokeh': 'visualization', 'Transoformed Network': 'deep learning', 'Bayesian Approaches': 'probability models','Fast.ai': 'deep learning',\
               'Geoplotlib': 'visualization', 'Automated Feature Engineering': 'automated tools','LightGBM': 'ensemble','Python': 'python', 'Pytorch': 'framework',\
               'Scikit-learn': 'framework', 'Evolutionary Approaches': 'ml','Decision Trees and Random Forest': 'ml', 'Automated Model Architecture Searches': 'automated tools',\
               'Generative Adversarial Networks': 'deep learning', 'Automated Data Augmentation': 'automated tools', 'Tensorflow': 'framework', 'Shiny': 'framework',\
               'Leaflet/Folium': 'visualization', 'Xgboost': 'ensemble', 'Plotly': 'visualization', 'Automated Model Selection': 'automated tools', 'Seaborn': 'visualization', 'Random Forest': 'ml',\
               'Linear Models': 'ml', 'C': 'c', 'ggplot': 'visualization', 'Java': 'java', 'cc++': 'c', 'Matplotlib': 'visualization', 'R': 'r', 'C++': 'c++', 'Javascript':'java'}

#Top grouped skills
top_skills = ['visualization', 'framework', 'big data']
top_skills_by_earlier_analysis = {'analytics': 0.21851428571428572, 'automated tools': 3.4303378215654083, 'big data': 3.1400963327859883,\
                                  'c': 0.9133539135194308, 'c++': 0.2816091954022989, 'cloud': 1.6064,\
                                  'deep learning': 4.387056814449918, 'ensemble method': 1.1726826491516147, 'excel': 3.093942857142857,\
                                  'framework': 4.780372632731254, 'java': 1.2577068418171866, 'matlab': 0.7900334975369459,\
                                  'ml': 4.590859332238643,'optimization': 0.6134857142857143,'probability model': 0.2425904761904762,\
                                  'probability models': 0.5911330049261084, 'python': 2.1597407772304322, 'r': 1.5596694033935412,\
                                  'scripting': 0.8336070060207992, 'simulation': 0.14110476190476187, 'sql': 3.597575916803503,\
                                  'statistics': 2.5773714285714284, 'time series': 0.0832, 'visualization': 5.597788724685277}

#Big weights topics sub topics by weights
visualization_topics = {'tableau': 'tableau', 'acumen': 'acumen', 'd3': 'd3', 'aws': 'aws', 'matplotlib': 'matplotlib',\
                        'seaborn': 'seaborn', 'bokeh': 'bokeh', 'ggplot': 'ggplot', 'plotly': 'plotly', 'geoplotlib': 'geoplotlib',\
                        'D3.js': 'd3', 'Bokeh': 'bokeh', 'Geoplotlib': 'geoplotlib', 'Leaflet/Folium': 'leaflet', 'Plotly': 'plotly',\
                        'Seaborn': 'seaborn', 'Matplotlib': 'matplotlib'}

v_subtopics ={'tableau': 1.3767976989453499, 'd3': 0.7313452573808974, 'bokeh': 0.6321875815048691,
             'aws': 0.5825077234473209, 'geoplotlib': 0.58128078817734, 'plotly': 0.5031683582944866,\
             'leaflet': 0.48440065681444994, 'seaborn': 0.45457768079846306, 'ggplot': 0.4444536280916749,\
             'matplotlib': 0.40779801853627357}

framework_topics = {'tensorflow': 'tensorflow', 'sap': 'sap', 'keras': 'tensorflow', 'nltk': 'nltk', \
                   'numpy': 'numpy', 'pandas': 'pandas', 'sklearn': 'sklearn', 'kafka': 'kafka',\
                   'scikit': 'scikit', 'scipy': 'scipy', 'Carcet': 'caret', 'Caret': 'caret', 'Keras': 'tensorflow',\
                   'Pytorch': 'pytorch', 'Scikit-learn': 'scikit', 'Tensorflow': 'tensorflow', 'Shiny': 'shiny'}

f_subtopics ={'tensorflow': 1.7667371970773962, 'caret': 0.8607006020799125, 'sap': 0.5552359646319378, 'scikit': 0.5469339475356602,\
             'pytorch': 0.5342090859332239,'shiny': 0.4854953475643131, 'kafka': 0.18962394801320975, 'pandas': 0.10525194417811867,\
             'numpy': 0.09417279215936937, 'scipy': 0.05454351763076595,'nltk': 0.021732182806008308,'sklearn': 0.006391818472355386}

bigdata_topics = {'spark': 'spark', 'hadoop': 'hadoop','data mining': 'mining', 'data manipulation': 'big data analytics', 'data wrangling': 'big data analytics', 'big data': 'big data analytics', \
             'information retrieval': 'big data analytics', 'interpreting data': 'big data analytics', 'Spark MLib': 'spark'}


bd_subtopics = {'big data analytics': 0.8097523809523811, 'hadoop': 0.470247619047619,\
                'mining': 0.5257142857142857, 'spark': 1.3136582375478927}

stop_word = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
              "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself',\
              'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
              'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',\
              'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',\
              'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',\
              'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',\
              'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',\
              'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',\
              'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',\
              'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll',\
              'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',\
              "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',\
              "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn',\
              "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'you', 'that', 'don', 'aren', 'couldn',\
              'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn',\
              'weren', 'won', 'wouldn', 'll', 't', 've']