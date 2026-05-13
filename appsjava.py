heads_="""
// apps.java


import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.util.*;
import java.util.Timer;
import java.util.TimerTask;

public class apps extends JFrame {

    static String source = "";
    private int score=0;
    private int fire=0;
    private int live=0;
    private int lives=3;
    private int x=0;
    private int y=0;
    private int z=0;
    private int w=0;
    private int h=0;
    private boolean ends=false;
    private int camera=0;
    private int enemy=0;
    private int enemycount=3;
    
    private int tsleep=100;

    
    Timer timer;

    void debugs(String c){
       System.out.println(c);
       try {
           ;//Thread.sleep(tsleep);
       }catch (Exception e){}
    }

"""
def saves(files,mode,value):
    f1=open(files,mode)
    f1.write(value)
    f1.close()


def heads(files,value):
    saves(files,"w",value)

print("give me the file name .txt ? ")
filesa=input().strip()


def getfiles(files):
    f1=open(files,"r")
    values=f1.read()
    f1.close()
    v=values.split("\n")
    return v
    

def defs(files,value):
    print("handle : function :"+value)
    
    saves(files,"a","void ")
    saves(files,"a",value)
    saves(files,"a"," (){\n")
    saves(files,"a",(" "*4)+"//put you code here\n")
    saves(files,"a",(" "*4)+ "debugs(\"")
    saves(files,"a",value)
    saves(files,"a","\");\n}\n")

print(filesa)
gfiles=getfiles(filesa)

filesa="apps.java"
heads(filesa,heads_)
for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs(filesa,sss)


heads__="""
    public apps() {

        setTitle("Mini Game Engine");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        DrawingCanvas canvas = new DrawingCanvas();
        add(canvas);

        parseGame();

        // ⏱️ loop do jogo (1 segundo)
        
        TimerTask task = new TimerTask() {
        public void run() {

"""

def defs_(files,value):
    print("handle : function :"+value)
    saves(files,"a","\n"+" "*12)
    
    saves(files,"a",value)
    saves(files,"a","();\n")

saves(filesa,"a",heads__)

for n in range(len(gfiles)):
    sss=gfiles[n].strip()
    if sss!="":
        defs_(filesa,sss)

heads___="""
            repaint();}
        };
        
        Timer timer = new Timer("Timer");
        long delay = 1000L;
        long period = 1000L;
        timer.scheduleAtFixedRate(task, delay, period);
    }

    void parseGame() {
        
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new apps().setVisible(true);
        });
    }

    // ==========================
    // Canvas
    // ==========================
    class DrawingCanvas extends JPanel {

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);

            // limpar ecrã
            g.setColor(Color.BLACK);
            g.fillRect(0, 0, getWidth(), getHeight());

           
        }
    }
}

"""
saves(filesa,"a",heads___)