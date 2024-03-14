fruit_dataset = {
    'Mango': {
        'Diseases': ['Anthracnose', 'Powdery Mildew', 'Fruit Fly Infestation'],
        'Fertilizer': {
            'Anthracnose': {
                'Fertilizer': ['Copper-based fungicides', 'Mancozeb', 'Azoxystrobin and Difenoconazole'],
            },
            'Powdery Mildew': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://assets-global.website-files.com/628ee8cd8f04ca5405cebd16/64f9a5b03f593ef7a7880de4_searles-wettable-sulphur-Product%20Image.webp']
            },
            'Fruit Fly Infestation': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            }
        }
    },
    'Apple': {
        'Diseases': ['Apple Scab', 'Fire Blight', 'Cedar Apple Rust'],
        'Fertilizer': {
            'Apple Scab': {
                'Fertilizer': ['Sulfur-based fungicides', 'Copper-based fungicides', 'Potassium phosphate'],
                'Image_URLs': [
                    'https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg',
                    'https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg',
                    'https://m.media-amazon.com/images/I/61VfyCVdQ2L._AC_UF1000,1000_QL80_.jpg'
                ]
            },
            'Fire Blight': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Calcium-containing fertilizers', 'Potassium-containing fertilizers'],
                'Image_URLs': [
                    'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg',
                    'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg',
                    'https://m.media-amazon.com/images/I/7134v94drOL.jpg'
                ]
            },
            'Cedar Apple Rust': {
                'Fertilizer': ['Balanced NPK fertilizers', 'Fertilizer with micronutrients like copper', 'Soil amendments with organic matter'],
                'Image_URLs': [
                    'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg',
                    'https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg',
                    'https://m.media-amazon.com/images/I/51xiSFSkJOL._SY445_SX342_QL70_FMwebp_.jpg'
                ]
            }
        }
    },
    'Banana': {
        'Diseases': ['Panama Disease (Fusarium wilt)', 'Black Sigatoka', 'Banana Bunchy Top Virus'],
        'Fertilizer': {
            'Panama Disease (Fusarium wilt)': {
                'Fertilizer': ['Potassium-rich fertilizers', 'Phosphorus-containing fertilizers', 'Organic compost'],
                'Image_URLs': [
                    'https://m.media-amazon.com/images/I/71F0ilMO3IS._SX522_.jpg',
                    'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg',
                    'https://m.media-amazon.com/images/I/51xiSFSkJOL._SY445_SX342_QL70_FMwebp_.jpg'
                ]
            },
            'Black Sigatoka': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Magnesium-containing fertilizers', 'Trace element fertilizers'],
                'Image_URLs': [
                    'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg',
                    'https://mahadhan.co.in/wp-content/uploads/2017/05/mahadhanmansulf.jpg',
                    'https://www.campbellsfert.com.au/wp-content/uploads/2017/05/Trace-It-Total-trimmed-v2.png'
                ]
            },
            'Banana Bunchy Top Virus': {
                'Fertilizer': ['High-potassium fertilizers', 'Calcium-containing fertilizers', 'Balanced NPK fertilizers'],
                'Image_URLs': [
                    'https://m.media-amazon.com/images/I/71F0ilMO3IS._SX522_.jpg',
                    'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg',
                    'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg'
                ]
            }
        }
    },
    'Orange': {
        'Diseases': ['Citrus Canker', 'Citrus Black Spot', 'Huanglongbing (Citrus Greening)'],
        'Fertilizer': {
            'Citrus Canker': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Citrus Black Spot': {
                'Fertilizer': ['Balanced NPK fertilizers', 'Micronutrient supplements', 'Foliar fertilizers with potassium and magnesium'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://agribegri.com/productimage/7607353b9bd9ad1e28d94cae9976e1aa-05-06-23-17-33-32.JPG', 'https://5.imimg.com/data5/TB/XR/MY-1393371/potassium-magnesium-sulphate-foliar-fertilizers.jpg']
            },
            'Huanglongbing (Citrus Greening)': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Guava': {
        'Diseases': ['Anthracnose', 'Guava Wilt', 'Fruit Fly Infestation'],
        'Fertilizer': {
            'Anthracnose': {
                'Fertilizer': ['Copper-based fungicides', 'Mancozeb', 'Azoxystrobin and Difenoconazole'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/SELLER/Default/2021/7/QW/GH/SA/6616513/mancozeb-75-wp-contact-fungicide-500x500.jpg', 'https://www.katyayaniorganics.com/wp-content/uploads/2022/06/Azozole-1536x1389-1.png']
            },
            'Guava Wilt': {
                'Fertilizer': ['Phosphorus-based fertilizers', 'Potassium-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Fruit Fly Infestation': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            }
        }
    },
    'Papaya': {
        'Diseases': ['Papaya Ringspot Virus', 'Powdery Mildew', 'Papaya Dieback'],
        'Fertilizer': {
            'Papaya Ringspot Virus': {
                'Fertilizer': ['Phosphorus-based fertilizers', 'Potassium-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Powdery Mildew': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://assets-global.website-files.com/628ee8cd8f04ca5405cebd16/64f9a5b03f593ef7a7880de4_searles-wettable-sulphur-Product%20Image.webp']
            },
            'Papaya Dieback': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Grapes': {
        'Diseases': ['Downy Mildew', 'Powdery Mildew', 'Botrytis Bunch Rot'],
        'Fertilizer': {
            'Downy Mildew': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Powdery Mildew': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://assets-global.website-files.com/628ee8cd8f04ca5405cebd16/64f9a5b03f593ef7a7880de4_searles-wettable-sulphur-Product%20Image.webp']
            },
            'Botrytis Bunch Rot': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Watermelon': {
        'Diseases': ['Gummy Stem Blight', 'Fusarium Wilt', 'Anthracnose'],
        'Fertilizer': {
            'Gummy Stem Blight': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Fusarium Wilt': {
                'Fertilizer': ['Phosphorus-based fertilizers', 'Potassium-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Anthracnose': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            }
        }
    },
    'Pineapple': {
        'Diseases': ['Pineapple Black Rot', 'Pineapple Wilt', 'Pink Disease'],
        'Fertilizer': {
            'Pineapple Black Rot': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Pineapple Wilt': {
                'Fertilizer': ['Phosphorus-based fertilizers', 'Potassium-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Pink Disease': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Pomegranate': {
        'Diseases': ['Bacterial Blight', 'Anthracnose', 'Fruit Rot'],
        'Fertilizer': {
            'Bacterial Blight': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Anthracnose': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://assets-global.website-files.com/628ee8cd8f04ca5405cebd16/64f9a5b03f593ef7a7880de4_searles-wettable-sulphur-Product%20Image.webp']
            },
            'Fruit Rot': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Lemon': {
        'Diseases': ['Citrus Canker', 'Citrus Black Spot', 'Lemon Scab'],
        'Fertilizer': {
            'Citrus Canker': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium sulfate', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/ANDROID/Default/2022/8/ZQ/PU/KH/5610246/product-jpeg-500x500.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Citrus Black Spot': {
                'Fertilizer': ['Balanced NPK fertilizers', 'Micronutrient supplements', 'Foliar fertilizers with potassium and magnesium'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://agribegri.com/productimage/7607353b9bd9ad1e28d94cae9976e1aa-05-06-23-17-33-32.JPG', 'https://5.imimg.com/data5/TB/XR/MY-1393371/potassium-magnesium-sulphate-foliar-fertilizers.jpg']
            },
            'Lemon Scab': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://assets-global.website-files.com/628ee8cd8f04ca5405cebd16/64f9a5b03f593ef7a7880de4_searles-wettable-sulphur-Product%20Image.webp']
            }
        }
    },
    'Strawberry': {
        'Diseases': ['Anthracnose', 'Botrytis Fruit Rot', 'Angular Leaf Spot'],
        'Fertilizer': {
            'Anthracnose': {
                'Fertilizer': ['Copper-based fungicides', 'Mancozeb', 'Azoxystrobin and Difenoconazole'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://5.imimg.com/data5/SELLER/Default/2021/7/QW/GH/SA/6616513/mancozeb-75-wp-contact-fungicide-500x500.jpg', 'https://www.katyayaniorganics.com/wp-content/uploads/2022/06/Azozole-1536x1389-1.png']
            },
            'Botrytis Fruit Rot': {
                'Fertilizer': ['Sulfur-based fungicides', 'Potassium bicarbonate', 'Wettable sulfur'],
                'Image_URLs': ['https://www.planetnatural.com/wp-content/uploads/2013/03/sulfur-fungicide.jpg', 'https://5.imimg.com/data5/KU/QE/RW/SELLER-21768957/11.jpg', 'https://']
            }
        }
    }
}

vegetable_dataset = {
    'Potato': {
        'Diseases': ['Late Blight', 'Early Blight', 'Potato Virus Y (PVY)'],
        'Fertilizer': {
            'Late Blight': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Early Blight': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Potato Virus Y (PVY)': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Tomato': {
        'Diseases': ['Tomato Blight', 'Tomato Yellow Leaf Curl Virus (TYLCV)', 'Septoria Leaf Spot'],
        'Fertilizer': {
            'Tomato Blight': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Tomato Yellow Leaf Curl Virus (TYLCV)': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Septoria Leaf Spot': {
                'Fertilizer': ['Phosphorus-containing fertilizers', 'Potassium-containing fertilizers', 'Nitrogen-based fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg']
            }
        }
    },
    'Onion': {
        'Diseases': ['Onion Downy Mildew', 'Onion White Rot', 'Onion Smut'],
        'Fertilizer': {
            'Onion Downy Mildew': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Onion White Rot': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Onion Smut': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Garlic': {
        'Diseases': ['Garlic Rust', 'Garlic White Rot', 'Stem and Bulb Nematode'],
        'Fertilizer': {
            'Garlic Rust': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Garlic White Rot': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Stem and Bulb Nematode': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Ginger': {
        'Diseases': ['Ginger Rhizome Rot', 'Pythium Rot', 'Bacterial Wilt'],
        'Fertilizer': {
            'Ginger Rhizome Rot': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Pythium Rot': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Bacterial Wilt': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Carrot': {
        'Diseases': ['Carrot Fly (Psila rosae)', 'Alternaria Leaf Blight', 'Carrot Black Rot'],
        'Fertilizer': {
            'Carrot Fly (Psila rosae)': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Alternaria Leaf Blight': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Carrot Black Rot': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Cabbage': {
        'Diseases': ['Black Rot of Cabbage', 'Clubroot', 'Downy Mildew'],
        'Fertilizer': {
            'Black Rot of Cabbage': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Clubroot': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Downy Mildew': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Cauliflower': {
        'Diseases': ['Clubroot', 'Downy Mildew', 'Alternaria Leaf Spot'],
        'Fertilizer': {
            'Clubroot': {
                'Fertilizer': ['Copper-based fungicides', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Downy Mildew': {
                'Fertilizer': ['Potassium-containing fertilizers', 'Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            },
            'Alternaria Leaf Spot': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Balanced NPK fertilizers', 'Organic fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71zxEAIaI7L._SX522_.jpg']
            }
        }
    },
    'Spinach': {
        'Diseases': ['Downy Mildew', 'Spinach Blight', 'Fusarium Wilt'],
        'Fertilizer': {
            'Downy Mildew': {
                'Fertilizer': ['Copper-based fungicides', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
                'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
            },
            'Spinach Blight': {
                'Fertilizer': ['Phosphorus-containing fertilizers', 'Nitrogen-based fertilizers', 'Calcium-containing fertilizers'],
                'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
            },
            'Fusarium Wilt': {
                'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium-containing fertilizers', 'Phosphorus-containing fertilizers'],
                'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg']
            }
        }
    },
    'Brinjal' : {
        'Diseases': ['Bacterial Wilt', 'Verticillium Wilt', 'Phomopsis Blight'],
    'Fertilizer': {
        'Bacterial Wilt': {
            'Fertilizer': ['Phosphorus-containing fertilizers', 'Potassium-containing fertilizers', 'Nitrogen-based fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg']
        },
        'Verticillium Wilt': {
            'Fertilizer': ['Calcium-containing fertilizers', 'Phosphorus-containing fertilizers', 'Potassium-containing fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/61keIPa9FbS.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg']
        },
        'Phomopsis Blight': {
            'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        }
    }
},
    'Capsicum' : {
    'Diseases': ['Anthracnose', 'Bacterial Spot', 'Phytophthora Blight'],
    'Fertilizer': {
        'Anthracnose': {
            'Fertilizer': ['Copper-based fungicides', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        },
        'Bacterial Spot': {
            'Fertilizer': ['Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
            'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
        },
        'Phytophthora Blight': {
            'Fertilizer': ['Phosphorus-containing fertilizers', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        }
    }
},
'Ladyfinger' : {
    'Diseases': ['Yellow Vein Mosaic Virus (YVMV)', 'Powdery Mildew', 'Fusarium Wilt'],
    'Fertilizer': {
        'Yellow Vein Mosaic Virus (YVMV)': {
            'Fertilizer': ['Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers', 'Calcium-containing fertilizers'],
            'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
        },
        'Powdery Mildew': {
            'Fertilizer': ['Potassium-containing fertilizers', 'Phosphorus-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        },
        'Fusarium Wilt': {
            'Fertilizer': ['Phosphorus-containing fertilizers', 'Potassium-containing fertilizers', 'Nitrogen-based fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg']
        }
    }
},
'Beetroot' : {
    'Diseases': ['Cercospora Leaf Spot', 'Rhizoctonia Root Rot', 'Beet Cyst Nematode'],
    'Fertilizer': {
        'Cercospora Leaf Spot': {
            'Fertilizer': ['Potassium-containing fertilizers', 'Phosphorus-containing fertilizers', 'Nitrogen-based fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg']
        },
        'Rhizoctonia Root Rot': {
            'Fertilizer': ['Calcium-containing fertilizers', 'Phosphorus-containing fertilizers', 'Potassium-containing fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/61keIPa9FbS.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg']
        },
        'Beet Cyst Nematode': {
            'Fertilizer': ['Nitrogen-based fertilizers', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        }
    }
},
'Cucumber' : {
    'Diseases': ['Powdery Mildew', 'Downy Mildew', 'Angular Leaf Spot'],
    'Fertilizer': {
        'Powdery Mildew': {
            'Fertilizer': ['Copper-based fungicides', 'Potassium-containing fertilizers', 'Balanced NPK fertilizers'],
            'Image_URLs': ['https://5.imimg.com/data5/GD/UT/MY-21033428/111-500x500.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/71Oc+zENm1L._AC_UF1000,1000_QL80_.jpg']
        },
        'Downy Mildew': {
            'Fertilizer': ['Phosphorus-containing fertilizers', 'Potassium-containing fertilizers', 'Calcium-containing fertilizers'],
            'Image_URLs': ['https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg', 'https://m.media-amazon.com/images/I/61keIPa9FbS.jpg']
        },
        'Angular Leaf Spot': {
            'Fertilizer': ['Nitrogen-based fertilizers', 'Phosphorus-containing fertilizers', 'Potassium-containing fertilizers'],
            'Image_URLs': ['https://www.arbico-organics.com/images/uploads/1300510_nitrogreen_600x600.jpg', 'https://m.media-amazon.com/images/I/719wTVdzkYL._AC_UF1000,1000_QL80_.jpg', 'https://m.media-amazon.com/images/I/7134v94drOL.jpg']
        }
    }
}
}