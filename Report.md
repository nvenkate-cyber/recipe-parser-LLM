## Where the LLM Approach Struggles:

Recipe: https://www.allrecipes.com/recipe/231154/creamy-chicken-cordon-bleu-casserole/

### Parsing issues:

- Can you direct me through the recipe at https://www.allrecipes.com/recipe/231154/creamy-chicken-cordon-bleu-casserole/
- Hello! I'd be happy to guide you through the Creamy Chicken Cordon Bleu Casserole recipe from Allrecipes.com.
- This recipe yields 8 servings. Are you ready to dive in, or would you like to see the ingredients first? __(correct servings)__

#### Representation does not match some recipes:

- How many steps in this? - gives an incorrect number (5): There are eight steps in the the actual directions. However, there are five overview steps. 
- What is step 5? - Gives an answer of Step 7 in the directions labeled at Step 5.
- What is the last step? - Gives the answer of Step 5 and then a description of Step 7. Step 7 is not the last step in the directions.


#### Step combination that destroys order:

- AI Step 3: Stir cooked chicken, ham, cream of chicken soup, milk, Swiss cheese, and cooked egg noodles in a large bowl. Pour the mixture into the prepared baking dish. Top with bread crumbs.
- AI Step 4: Melt butter in a medium saucepan over medium heat. Stir in flour, salt, and black pepper; cook and stir until smooth, about 2 minutes. Gradually whisk in chicken broth and bring to a boil; cook and stir until thickened, about 2 minutes. Remove from heat and pour over the casserole. 
- These are a combination of:
- Recipe Step 4: Top noodles with chicken, ham, and Swiss cheese.
- Recipe Step 5: Mix together condensed soup, milk, and sour cream in a medium bowl until combined; spoon over noodle mixture in the casserole dish.
- Recipe Step 6: Melt butter in a skillet over medium heat; cook and stir bread crumbs and Parmesan cheese in hot butter until crumbs are well coated, 2 to 3 minutes. Sprinkle over casserole.


#### Parse changes ingredients:

LLM ingredients:
*   1 (12 ounce) package extra-wide egg noodles
*   4 cups cooked chicken, diced
*   1 1/2 cups cooked ham, diced
*   1 (10.75 ounce) can condensed cream of chicken soup
*   1/2 cup milk
*   1 1/2 cups shredded Swiss cheese
*   1/2 cup dry bread crumbs
*   1/4 cup butter
*   1/4 cup all-purpose flour
*   1 teaspoon salt
*   1/4 teaspoon ground black pepper
*   2 cups chicken broth

Recipe Ingredients:
*   1 (8 ounce) package wide egg noodles
*   2 cups chopped cooked chicken breast
*   8 ounces cooked ham, cubed
*   8 ounces Swiss cheese, cubed
*   1 (10.5 ounce) can reduced-fat, reduced-sodium cream of chicken soup
*   1/2 cup 2% milk
*   1/2 cup light sour cream
*   2 tablespoons butter
*   1/3 cup seasoned bread crumbs
*   1/4 cup grated Parmesan cheese

These parsing issues indicate that it may not be directly parsing the recipe, but rather aggregating similar recipes and displaying that.
    
### Relevance based on Step # 

__(At LLM Step 4): Melt butter in a medium saucepan over medium heat...__
- What is the most relevant temp?
- The most relevant temperature, given in specific degrees, is the **oven temperature of 350 degrees F (175 degrees C)**. 
It depends a little on what you consider a temp and how you define relevance, but the natural answer seems like it should be "medium heat" given that you are not using the oven in this step. The LLM is aware of Medium Heat as a temperature because it answers correctly on "What is the most relevant temp for step 4?" This indicates it may not be directly keeping track of steps.


## What the LLM approach does better:


### Substitutions

Invents reasonable substitutions. Also understands Vegetarian/Vegan substitution options: 
- What can I substitute for chicken if I am vegetarian?
- Plant-Based Chicken Substitutes: Look for vegetarian or vegan chicken strips or pieces in the frozen or refrigerated section of your grocery store. Brands like Gardein, MorningStar Farms, or Beyond Meat often have good options that will mimic the texture well. You'll want to dice them just like the cooked chicken.
The parser may be able to compete if it had a large dataset of substitutions built in, but the LLM has a better understanding of "Vegetarian" and can find better substitutes.

### Understanding Vague Phrases

__(At LLM Step 4)__
- What was the temp? 
- The oven temperature for this recipe is **350 degrees F (175 degrees C)**, as stated in Step 1.
- For Step 4, where you're making the sauce on the stovetop, you'll be using **medium heat** for your saucepan.
The AI has the advantage where it can list multiple responses to answer questions with vagueness or multiple relevant options, which dispenses vagueness.

### Recognizing safety concerns outside of the recipe

__(At LLM Step 1)__ "Preheat an oven to 350 degrees F (175 degrees C). Lightly grease a 9x13-inch baking dish."
- Can I spray the grease on the dish once it is in the oven to be more efficient?
- That's an interesting thought for efficiency, but I strongly recommend **against** spraying grease on the dish once it's already in a hot oven.
  Here's why:
  1.  **Safety Hazard:** Aerosol cooking sprays are highly flammable, and spraying them into a hot oven can create a fire risk.
  2.  **Ineffective Coating:** The heat from the oven would cause the grease to evaporate or burn off almost immediately, preventing it from properly coating the dish and creating the non-stick layer you need.
The LLM has more information at it's disposal about how things may interact (like aerosol and heat) and can make those distinctions where the parser cannot.
