
# coding: utf-8

# In[2]:


from IPython.display import HTML

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from IPython.html import widgets

t = np.arange(0.0, 1.0, 0.01)

def pltsin(f):
    plt.plot(t,np.sin(2*np.pi*t*f))
    plt.show()

widgets.interact(pltsin, f=(1,10,0.1))

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')

