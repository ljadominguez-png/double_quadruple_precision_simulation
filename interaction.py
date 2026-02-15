import streamlit as st  
import time
from calculations import *

if 'page' not in st.session_state:
    st.session_state.page = 'home'

#typing animation function
def type(text, delay):
    placeholder = st.empty()
    typed_text = ''
    for char in text:
        typed_text += char
        placeholder.markdown(f"##### {typed_text}")
        time.sleep(0.05)#the speed of typing
    time.sleep(delay)#delay after typing is done

def home():
    st.session_state.page = 'home'
def simulation():
    st.session_state.page = 'simulation'
def references():    
    st.session_state.page = 'references'
def how():
    st.session_state.page = 'how'
def double_precision():
    st.session_state.page = 'double'
def quadruple_precision():
    st.session_state.page = 'quadruple'

if st.session_state.page == 'home':
    
    st.title("Double and Quadruple Precision Floating Point Representation Simulator")
    st.markdown("___")
    st.write("""
    This simulator demonstrates how double and quadrupleprecision 
    floating point numbers are represented in computer 
    memory according to the IEEE 754 standard.""")
    col1, col2 , col3 = st.columns(3)
    with col1:
        if st.button("how does this work?"):
            how()
            st.rerun()
    with col2:
        if st.button("Start Simulation"):
            simulation()
            st.rerun()  
    with col3:
        if st.button("references"):
            references()
            st.rerun()

elif st.session_state.page == 'how':
    st.header("How does this work?")       

    if st.button("explain"):
        type("The Patriot Missile incident is a tragic example of how a small error in floating point representation can have catastrophic consequences.", 0.5)
        type("In 1991, a Patriot Missile missed its target", 0.5)
        type("This happened because of a floating point error in the system's timekeeping.", 0.5)
        type("This incident became a wake up call for the importance of floating point precision in critical systems.", 0.5)
        type("Which makes 64 bit floating point numbers became standard for military and aerospace applications.", 0.5)
        st.markdown(f"##### This video shows how the incident occured")
        st.video("assets/MIM-104 Patriot vs Scud_Al Hussein SRBM Operation Desert Storm - jaglavaksoldier (480p, h264).mp4")
        type("A precision error had caused 28 lives to be lost.", 0.5)
    if st.button("back"):
        home()
        st.rerun()
    

elif st.session_state.page == 'simulation':
    st.header("Simulation")
    st.markdown(f"#### Choose among the following options.")
    st.markdown("___")
    col1, col2 , col3 = st.columns(3)
    with col1:
        if st.button("Double Precision"):
            double_precision()
            st.rerun()
    with col2:
        if st.button("Quad Precision"):
            quadruple_precision()
            st.rerun()  
    with col3:
        if st.button("Back to home"):
            home()
            st.rerun()


elif st.session_state.page == "references":
    st.header("Academic References")
    
    st.subheader("1. 24-bit Precision & Patriot Missile Analysis")
    st.markdown("""
    * **Arnold, D. N. (2000).** [The Disaster of the Patriot Missile](https://www-users.cse.umn.edu/~arnold/disasters/patriot.html)
    * **Institute of Electrical and Electronics Engineers. (1985).** [IEEE Standard 754-1985 for Binary Floating-Point Arithmetic](https://ieeexplore.ieee.org/document/30711)
    * **Marshall, E. (1992).** [Fatal Error: How Patriot Missed](https://www.science.org/doi/10.1126/science.255.5050.1347)
    * **Skeel, R. D. (1992).** [Roundoff Error and the Patriot Missile](https://faculty.math.illinois.edu/~skeel/skeel_patriot.pdf)
    * **U.S. General Accounting Office. (1992).** [Patriot Missile Defense: Software Problem Led to System Failure at Dhahran](https://www.gao.gov/products/imtec-92-26)
    """)

    st.subheader("2. 64-bit & 128-bit Standards (NASA/Supercomputing)")
    st.markdown("""
    * **Gupta, A. (2019).** [What’s the Difference Between Single, Double, Multi and Mixed Precision Computing?](https://blogs.nvidia.com/blog/whats-the-difference-between-single-double-multi-and-mixed-precision-computing/)
    * **HPCwire. (2018).** [The Role of Quadruple Precision in Future Exascale Computing](https://www.hpcwire.com/2018/06/13/why-the-worlds-fastest-supercomputer-matters/)
    * **Institute of Electrical and Electronics Engineers. (2019).** [IEEE Standard 754-2019 for Floating-Point Arithmetic](https://ieeexplore.ieee.org/document/8766229)
    * **Muller, J. M. (2018).** [Handbook of Floating-Point Arithmetic (2nd ed.)](https://link.springer.com/book/10.1007/978-3-319-76526-6)
    * **NASA Jet Propulsion Laboratory. (2022).** [How Many Decimals of Pi Do We Really Need?](https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/)
    """)
    
    if st.button("Back to Home"):
        home()
        st.rerun()

elif st.session_state.page == "double":
    st.header("Double Precision Simulation")
    st.write("Take note 0.0 means no drift, the smaller the number the better.")
    hours = st.slider(f"## Select the System Runtime Hours", min_value = 0, max_value = 100, value = 1)
    if st.button("simulate"):
        st.write(f"Simulating for {hours} hours of continuous operation.")
        st.markdown("___")
        #for the 24 bit simulation
        val_24 = twentyfourbits('0.1')
        bin_24 = twentyfbits(val_24)
        #for the 64bit simulation
        val_64 = doubleprecision('0.1')
        bin_64 = sixtyfourbits(val_64)
        #drift calculation
        target = Decimal('0.1')
        total_ticks = hours * 3600 * 10 #Multiplying by 3,600 converts the Hours to seconds * 10 because 10 ticks per second

        drift_24 = abs(target - Decimal(str(bin_24))) * total_ticks
        drift_64 = abs(target - Decimal(str(bin_64))) * total_ticks

        #the seconds
        st.markdown(f"### 1. Memory Analysis")
        type("Comparing how 24-bit and 64-bit hardware store the value", 0.0)
        col1, col2 = st.columns(2)
        with col1:
            st.error("**24-bit**")
            st.code(f"Total drift: {drift_24:.20f}s")
        with col2:
            st.success("**64-bit**")
            st.code(f"Total drift: {drift_64:.20f}s")

        #the binary representation
        st.markdown(f"### 2. Binary Representation")
        type("Comparing the binary representation of 0.1 in 24-bit and 64-bit hardware", 0.0)
        col1, col2 = st.columns(2)
        with col1:
            st.error("**24-bit**")
            st.code(val_24)
        with col2:
            st.success("**64-bit**")
            st.code(val_64)
        #the graph
        st.markdown(f"### 3. Graphical Representation")
        type("Visualizing the drift over time for 24-bit and 64-bit hardware", 0.0)
        chart_data = []# without the loop the drift will just be one point, so we need to calculate the drift for each hour and store it in a list to create the graph
        for h in range(hours + 1): #+1 so that it does not start with 0 hours of runtime
            ticks = h * 3600 * 10
            drift_24_h = abs(target - Decimal(str(bin_24))) * ticks
            drift_64_h = abs(target - Decimal(str(bin_64))) * ticks
            chart_data.append({"Hours": h, "24-bit Drift (s)": float(drift_24_h), "64-bit Drift (s)": float(drift_64_h)})
        st.line_chart(chart_data, x="Hours", y=["24-bit Drift (s)", "64-bit Drift (s)"])
    if st.button("back"):
        simulation()
        st.rerun()

elif st.session_state.page == "quadruple":
    st.header("Quadruple Precision Simulation")
    st.write("Take note 0.0 means no drift, the smaller the number the better.")
    hours = st.slider(f"## Select Mission Duration (years)", min_value = 0, max_value = 50000000000, value = 1)#fifty billion years is the estimated remaining lifespan of the sun, so that is the maximum value for the slider
    
    if st.button("simulate"):
        st.write(f"Simulating for {hours} years of continuous operation.")
        bin_64 = doubleprecision('0.1')
        val_64 = sixtyfourbits(bin_64)
        bin_128 = quadprecision('0.1')
        val_128 = onetwoeitybits(bin_128)
        # 60 * 60 = 3600 seconds in an hour, 3600 * 24 = 86400 seconds in a day, 365 * 86400 = 31536000 seconds in a year
        total_seconds = hours * 31536000

        drift_64 = abs(Decimal('0.1') - Decimal(str(val_64))) * total_seconds
        drift_128 = abs(Decimal('0.1') - Decimal(str(val_128))) * total_seconds
        st.markdown(f"### 1. Memory Analysis")
        type("Comparing how 64-bit and 128-bit hardware store the value", 0.0)
        col1, col2 = st.columns(2)
        with col1:
            st.error("**64-bit**")
            st.code(f"Total drift: {drift_64:.20f}s")
        with col2:
            st.success("**128-bit**")
            st.code(f"Total drift: {drift_128:.20f}s")
        st.markdown(f"### 2. Binary Representation")
        type("Comparing the binary representation of 0.1 in 64-bit and 128-bit hardware", 0.0)
        col1, col2 = st.columns(2)
        with col1:
            st.error("**64-bit**")
            st.code(bin_64)
        with col2:
            st.success("**128-bit**")
            st.code(bin_128)
            #the graph
        st.markdown(f"### 3. Graphical Representation")
        type("Visualizing the drift over time for 64-bit and 128-bit hardware", 0.0)
        chart_data = []# without the loop the drift will just be one point, so we need to calculate the drift for each year and store it in a list to create the graph
        steps = max(1, hours // 100) # to avoid having too many points on the graph, we will only calculate the drift for every 1% of the total hours
        for h in range(0, hours + 1, steps): #+1 so that it does not start with 0 years of runtime
            seconds = h * 31536000
            drift_64_h = abs(Decimal('0.1') - Decimal(str(val_64))) * seconds
            drift_128_h = abs(Decimal('0.1') - Decimal(str(val_128))) * seconds
            chart_data.append({"Years": h, "64-bit Drift (s)": float(drift_64_h), "128-bit Drift (s)": float(drift_128_h)})
        st.line_chart(chart_data, x="Years", y=["64-bit Drift (s)", "128-bit Drift (s)"])
    if st.button("back"):
        simulation()
        st.rerun()



