# StackAndQueues
Stack And Queues

**การทำงานของอัลกอริทึม**

  - รับค่า ข้อความ
  - ตั้ง ตัวแปร is_error เป็น false และ location เป็น ลิสต์ และ stack เป็น class Stack
  - นำข้อความมาวนลูป
  - ให้ ตัวแปร s มีค่าเป็น ตัวอักษรปัจจุบัน
  - ตรวจสอบว่าตัวอักษรนั้นเป็นตัว ( หรือ [ หรือ { ถ้าเป็น ให้ ยัดค่า ตัวอักษรเข้าไปใน stack โดยใช้ push()
  - ในกรณีที่ตรวจสอบข้อข้างบนแล้วไม่เป็น ให้ตรวจสอบว่าตัวอักษรนั้นเป็นตัว ) หรือ ] หรือ } ถ้าเป็น
    ให้ตรวจสอบว่า stack เป็น ค่าว่าหรือไม่ ถ้า ไม่เป็น ให้ ตัวแปร p มีค่าเป็น stack ตัวล่าสุดที่ยัดค่าเข้าไปก่อนหน้า (โดยใช้ pop) ถ้าไม่ใช่ ตัวแปร  p มีค่าว่าง      เปล่า
  - ยัดค่าตัวอักษรใส่ใน ลิสต์ location
  - ตรวจวสอบว่า ค่าของ p เป็น ( และ s เป็น ) หรือ  p เป็น [ และ s เป็น ] หรือ  p เป็น { และ s เป็น }
      ถ้าเป็น ให้ลบ ข้อมูลตัวล่าสุด ของ location ออก
      ถ้าไม่เป็น ให้ is_error มีค่าเป็น true
  - เมื่อวนลูปเสร็จสิ้น ให้ตรวจสอบว่า stack เป็นค่าว่างหรือไม่ ถ้าเป็น ให้ is_error เป็น true และ ให้ ยัดค่าตำแหน่งสุดท้ายไปใน location
  - แล้ว return ค่าของ is_error และ location ออกมา

**การทดสอบ**
  ครั้งที่ 1
    ข้อความ = '[{(Hello)}]'
    <br>
    is_error เป็น False
    <br>
    Location เป็น []
    <br>
    ![image](https://github.com/Mewwemmew/StackAndQueues/assets/150503581/0dffa0a0-fde8-4daf-b6e6-59b2acffe690)

 ครั้งที่ 2
    ข้อความ = '[{(Hello})]'
     <br>
    is_error เป็น True
    <br>
    Location เป็น [8,9]
    <br>
    ![image](https://github.com/Mewwemmew/StackAndQueues/assets/150503581/4a3fe422-50be-458a-9591-e30a8d1dadec)
    
 ครั้งที่ 3
    ข้อความ = '[{(Hello'
     <br>
    is_error เป็น True
    <br>
    Location เป็น [7]
    <br>
    ![image](https://github.com/Mewwemmew/StackAndQueues/assets/150503581/545f67c0-43a1-4d2a-8a25-f029e04bb8d3)
    
 ครั้งที่ 4
    ข้อความ = 'Hello)('
     <br>
    is_error เป็น True
    <br>
    Location เป็น [5,6]
    <br>
    ![image](https://github.com/Mewwemmew/StackAndQueues/assets/150503581/33ea6dbc-9b61-4469-9950-6a4175e7e433)
    
 ครั้งที่ 5
    ข้อความ = '{}{'
     <br>
    is_error เป็น True
    <br>
    Location เป็น [2]
    <br>
    ![image](https://github.com/Mewwemmew/StackAndQueues/assets/150503581/b64fb445-f1a5-4032-943b-ba5702f2b797)



