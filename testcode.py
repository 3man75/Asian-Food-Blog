    
def Rest():
    
    Restaurants1 = {'Name': 'Chow', 
                  'Description' : """Chow One is a Korean Steakhouse with an all you can eat buffet some some particular breadth in options. Like
                  others of its kind it sports a Table-Grill that customers can cook there food on. Options include fish, chicken, and pork all 
                  greatly delicious."""
                   , 
                  'ChowOneImg' : url_for('static', filename='Chow.jpeg')
    }
    Restaurants2 = {'Name': 'Da Teng Wei', 
                  'Description' : """A Chinese Restaurant located in Brickel. Featuring high end contemporary Chinese foods with different regional specialties."""
                   , 
                  'DaTengZhenWeiImg' : url_for('static', filename='Da Teng Zhen Wei.jpg')
    }
    Restaurants3 = {'Name': 'Fuchai Miami', 
                  'Description' : """Fuchai Miami is a Southeast Asian Restaurant that focuses its menu on a Fusion of Chinese and Korean Foods. 
                  They have also have vegan and vegetarian options as well as a kids menu."""
                   , 
                  'FuchaiImg' : url_for('static', filename='Fuchai_Miami.jpg')
    }
    Restaurants4 = {'Name': 'Hutong Miami', 
                  'Description' : """Hutong Miami is a Chinese Restaurant with an emphasis of cocktails from Hong Kong, London, and New York. 
                  Hutong stays true to its Chinese roots with its menu while embracing the Miami ambience."""
                   , 
                  'HutonImg' : url_for('static', filename='Huton_Miami.jpg')
    }
    Restaurants5 = {'Name': 'Komodo', 
                  'Description' : """Southeast Asian Restaurant in Downtown Miami. Komodo was a little pricey and its location leaves little room for parking.
                  I recomend using an Uber or Carpool for a day to Komodo. 
                  The Food however made up for it at the time as they do have some nice pieces in their menu. 
                  They also have have fusion meals that combine Asian foods with local Latin foods."""
                   , 
                  'KomodoImg' : url_for('static', filename='komodo.jpg')
    }
    Restaurants6 = {'Name': 'Shima', 
                  'Description' : """One of my all time favorite restaurants for Asian food in Miami albeit a little far from previously mentioned locations. 
                  Shimaa serves traditional Japanese food and even comes with small little boats as extra platters that guests can take for themselves. 
                  My favorite part are the littble boats that trail in a circle in the store with small plates of food. Customers can reach out  ."""
                   , 
                  'ShimaImg' : url_for('static', filename='Shima.jpeg')
    }
    Restaurants7 = {'Name': 'Tanuki', 
                  'Description' : """Tanuki is an Asian fusian restaurant of all of the dishes from Asia. 
                  This includes Japanese, Chinese, and SouthEastern Dishes. 
                  The Tanuki mascot is also really cute in my opinion because it reminds me of Pokemon and Super Mario."""
                   , 
                  'TanukiImg' : url_for('static', filename='Tanuki.jpeg')
    }
    Restaurants8 = {'Name': 'Yip Dim Sum', 
                  'Description' : """With a Location in Doral Yip Dip Sun brings Chinese cuisine a little closer to home for me. 
                  After visitting with a freind I ended up enjoying their Boba tea's and their Dumplings best."""
                   , 
                  'YipDoralSumImg' : url_for('static', filename='Yip_Doral.jpg')
    }
    
    rest_object = Restaurants1, Restaurants2, Restaurants3, Restaurants4, Restaurants5, Restaurants6, Restaurants7, Restaurants8
    
    return rest_object
    ## <div class="w3-center w3-padding-32">
 ##   <div class="w3-bar">
##      <a href="#" class="w3-bar-item w3-button w3-hover-black">&laquo;</a>
 ##     <a href="#" class="w3-bar-item w3-black w3-button">1</a>
 ##     <a href="#" class="w3-bar-item w3-button w3-hover-black">2</a>
 ##     <a href="#" class="w3-bar-item w3-button w3-hover-black">3</a>
 ##     <a href="#" class="w3-bar-item w3-button w3-hover-black">4</a>
 ##     <a href="#" class="w3-bar-item w3-button w3-hover-black">&raquo;</a>
 ##   </div>
##  </div>